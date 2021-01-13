from django.db import models
from courses.models.course_model import Course


class Video(models.Model):
    title = models.CharField(max_length=256, null=False)
    course_id = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)
    serial_number = models.IntegerField(null=False)
    video_url = models.CharField(max_length=256, null=False)
    is_preview = models.BooleanField(default=False)
