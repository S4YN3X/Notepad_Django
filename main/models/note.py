import uuid

from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField


class Note(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название заметки')
    text = RichTextField(verbose_name='Текст заметки', blank=True, null=True)
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.RESTRICT)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'