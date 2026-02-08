from django.contrib import admin
from django.urls import path, include
from apps.words.views import home

urlpatterns = [
    path("admin/", admin.site.urls),

    # allauth routes (login, logout, google oauth)
    path("accounts/", include("allauth.urls")),

    path("words/", include("apps.words.urls")),

    # home page
    path("", home),
]

