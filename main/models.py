from django.db import models
from django.urls import reverse_lazy

class Stories(models.Model):
	title = models.CharField(max_length=150, verbose_name='Название')
	slug = models.SlugField(max_length=150, verbose_name='Url', default='')
	text = models.TextField(verbose_name='Контент')
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
	updated_at = models.DateTimeField(auto_now=True, verbose_name='Изменено')
	image = models.ImageField(upload_to='images/%Y/%m/%d', verbose_name='Изображения')
	is_published = models.BooleanField(default=False, verbose_name='Опубликовать')
	views = models.IntegerField(default=0, verbose_name='Количество просмотров')
	category = models.ManyToManyField('Category', blank=True,
									  related_name='stories', verbose_name='Категории')

	def get_absolute_url(self):
		return reverse_lazy('view_story', kwargs={"slug": self.slug})

	def __str__(self):
		return self.title

	class Meta():
		verbose_name = 'История'
		verbose_name_plural = 'Истории'
		ordering = ['-created_at']

		
class Category(models.Model):
	title = models.CharField(max_length=100, db_index=True, verbose_name='Название категории')
	slug = models.SlugField(max_length=100, verbose_name='Url', default='')

	def get_absolute_url(self):
		return reverse_lazy('category', kwargs={"slug": self.slug})
	
	def __str__(self):
		return self.title
	
	class Meta():
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'
		ordering = ['title']


class Comment(models.Model):
	stories = models.ForeignKey(Stories, on_delete=models.CASCADE,
								verbose_name='Статья', related_name='comment_story')
	author = models.CharField(max_length=30, verbose_name= 'Автор')
	content = models.TextField(verbose_name='Текст комментария:')
	is_active = models.BooleanField(default=True, db_index=True,
									verbose_name='Выводить на экран?')
	created_at = models.DateTimeField(auto_now_add=True, db_index=True,
									  verbose_name='Опубликован')

	class Meta:
		verbose_name_plural = 'Комментарии'
		verbose_name = 'Комментарий'
		ordering = ['created_at']