from django.contrib import admin
from django.urls import path
from courses.views import home_view, course_view


urlpatterns = [
    path('', home_view, name="home"),
    path('course/<str:slug>', course_view, name="course"),
]
