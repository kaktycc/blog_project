from django.db import models
from django.contrib import admin


class Post(models.Model):
    title = models.CharField(verbose_name='Название статьи', max_length=100)
    description = models.TextField(verbose_name='Содержание статьи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    image = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Изображение', blank=True)

    def __str__(self):
        return f'{self.title} ({self.created_at})'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'image']
