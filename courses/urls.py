from django.contrib import admin
from django.urls import path
from courses.views import index

urlpatterns = [
    path('', index.home_view, name="home"),
]
