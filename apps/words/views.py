from django.shortcuts import render, get_object_or_404
from .models import Word

def home(request):
    return render(request, "home.html")

def word_detail(request, slug):
    word = get_object_or_404(Word, slug=slug)
    return render(request, "words/detail.html", {"word": word})

def word_examples(request, slug):
    word = get_object_or_404(Word, slug=slug)
    return render(request, "words/examples.html", {"word": word})

