from django.urls import path
from .views import *

urlpatterns = [
	path('register/', register, name='register'),
	path('login/', user_login, name='login'),
	path('logout/', user_logout, name='logout'),
	path('mail/', user_mail, name='mail'),
	path('', Index.as_view(), name='home'),
	path('category/<str:slug>', StoriesByCategory.as_view(), name='category'),
	path('stories/<str:slug>', ViewStory.as_view(), name='view_story'),
	path('stories/add-story/', CreateStory.as_view(), name='add_story'),
	path('search/', Search.as_view(), name='search'),
]