from django.contrib import admin
from django.urls import path

from .views import login, sample_api

urlpatterns = [
    path('login', login),
    path('sample', sample_api)
]
