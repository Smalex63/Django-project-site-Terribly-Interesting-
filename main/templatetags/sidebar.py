from django import template

from main.models import Stories

register = template.Library()

@register.inclusion_tag('main/popular.html')
def get_popular_posts(cnt=5):
    posts = Stories.objects.order_by('-views')[:cnt]
    return {'posts': posts}