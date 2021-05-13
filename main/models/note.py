from django.db import models
from django.conf import settings


class Note(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название заметки')
    text = models.TextField(verbose_name='Текст заметки')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Автор', on_delete=models.RESTRICT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'