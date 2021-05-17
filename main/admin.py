from django.contrib import admin
from main.models.note import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['name', 'author']
    list_display_links = ['name', 'author']