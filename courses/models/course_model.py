from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=256, null=False)
    slug = models.CharField(max_length=256, null=False, unique=True)
    description = models.CharField(max_length=256, null=False)
    price = models.IntegerField(null=False)
    discount = models.IntegerField(null=False, default=0)
    active = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to="files/thumbnails")
    resource = models.FileField(upload_to="files/resources")
    length = models.IntegerField(null=False)

    def __str__(self):
        return self.name


class CourseProperty(models.Model):
    description = models.CharField(max_length=256, null=False)
    course_id = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Tag(CourseProperty):
    pass


class Prerequisite(CourseProperty):
    pass


class Learning(CourseProperty):
    pass
