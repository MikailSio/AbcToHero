from django.db import models

class Word(models.Model):
    word = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)
    meaning = models.TextField()
    level = models.CharField(max_length=10, blank=True)
    image_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.word
