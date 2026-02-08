from django.contrib import admin
from .models import Word

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ("word", "meaning", "level", "created_at")
    search_fields = ("word", "meaning")
    prepopulated_fields = {"slug": ("word",)}
