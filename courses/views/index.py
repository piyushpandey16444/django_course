from django.shortcuts import render, HttpResponse
from courses.models.course_model import Course


def home_view(request):
    course_obj = Course.objects.all()
    context = {
        'courses': course_obj,
    }
    return render(request, "courses/index.html", context=context)
