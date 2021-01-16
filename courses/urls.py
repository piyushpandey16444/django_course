from django.contrib import admin
from django.urls import path
from courses.views import *


urlpatterns = [
    path('', home_view, name="home"),
    path('course/<str:slug>', course_view, name="course"),
    path('signup/', signup_view, name="signup"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
]
