from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=256, null=False)
    description = models.CharField(max_length=256, null=True)
    price = models.IntegerField(null=False)
    discount = models.IntegerField(null=False, default=0)
    active = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to="files/thumbnails")
    resource = models.FileField(upload_to="files/resources")
    length = models.IntegerField(null=False)
