from django.shortcuts import render, HttpResponse, get_object_or_404
from courses.models.course_model import Course


def course_view(request, slug):
    course_obj = get_object_or_404(Course, slug=slug)
    context = {
        'course_detail': course_obj,
    }
    return render(request, 'courses/course_page.html', context)
