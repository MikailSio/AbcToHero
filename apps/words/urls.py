from django.urls import path
from . import views

app_name = "words"

urlpatterns = [
    path("<slug:slug>/", views.word_detail, name="detail"),
    path("<slug:slug>/examples/", views.word_examples, name="examples"),
]

