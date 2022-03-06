from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.db.models import F
from django.urls import reverse_lazy

from .models import Stories, Category
from .forms import StoryForm, UserRegisterForm, UserLoginForm, ContactForm, CommentForm


def user_mail(request):
	if request.method == 'POST':
		form = ContactForm(data=request.POST)
		if form.is_valid():
			mail = send_mail(form.cleaned_data['subject'], form.cleaned_data[
				'text'], 'smalexalex1980@yandex.ru', ['79869525925@yandex.ru'], fail_silently=True)
			if mail:
				messages.success(request, 'Письмо успешно отправлено!')
				return redirect('home')
			else:
				messages.error(request, 'Ошибка отправления!')
	else:
		form = ContactForm()
	return render(request, 'main/mail.html',  {'form': form})
	
	
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, 'Поздравляем. Вы успешно зарегистрировались!')
			return redirect('home')
		else:
			messages.error(request, 'Ошибка регистрации')
	else:
		form = UserRegisterForm()
	return render(request, 'main/register.html', {'form': form})
	

def user_login(request):
	if request.method == 'POST':
		form = UserLoginForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect('home')
	else:
		form = UserLoginForm()
	return render(request, 'main/login.html',  {'form': form})
	
	
def user_logout(request):
	logout(request)
	return redirect('home')


class Index(ListView):
	model = Stories
	template_name = 'main/index.html'
	context_object_name = 'stories'
	paginate_by = 5

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Страшно интересно'
		return context

	def get_queryset(self):
		return Stories.objects.filter(is_published=True)


class StoriesByCategory(ListView):
	template_name = 'main/index.html'
	context_object_name = 'stories'
	allow_empty = False
	paginate_by = 5

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = Category.objects.get(slug=self.kwargs['slug'])
		return context

	def get_queryset(self):
		return Stories.objects.filter(category__slug=self.kwargs['slug'], is_published=True)


class ViewStory(FormMixin, DetailView):
	model = Stories
	template_name = 'main/view_story.html'
	context_object_name = 'story_item'
	form_class = CommentForm

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		self.object.views = F('views') + 1
		self.object.save()
		self.object.refresh_from_db()
		return context

	def get_success_url(self, **kwargs):
		return reverse_lazy('view_story', kwargs={'slug': self.get_object().slug})
	
	def post(self, request, *args, **kwargs):
		form = self.get_form()
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.stories = self.get_object()
		self.object.author = self.request.user
		self.object.save()
		return super().form_valid(form)


class CreateStory(LoginRequiredMixin, CreateView):
	form_class = StoryForm
	template_name = 'main/add_story.html'
	success_url = reverse_lazy('home')


class Search(ListView):
	template_name = 'main/search.html'
	context_object_name = 'stories'
	paginate_by = 5

	def get_queryset(self):
		return Stories.objects.filter(text__icontains=self.request.GET.get('s'))

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['s'] = f"s={self.request.GET.get('s')}&"
		return context