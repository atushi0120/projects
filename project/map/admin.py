from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('user','title')
    list_display_links = ('user','title')

admin.site.register(Article,ArticleAdmin)
# Register your models here.
