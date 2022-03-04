from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.utils.safestring import mark_safe

from .models import Stories, Category, Comment


class StoriesAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Stories
        fields = '__all__'


class StoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    form = StoriesAdminForm
    list_display = ('id', 'title', 'slug', 'created_at', 'updated_at', 'is_published', 'views', 'get_image')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'text')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')

    
    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50">')
        return '-'
    	
    get_image.short_description = 'Изображение'
    
    
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'stories', 'is_active')
    list_editable = ('is_active',)
    

admin.site.register(Stories, StoriesAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
