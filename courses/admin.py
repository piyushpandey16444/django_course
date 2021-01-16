from django.contrib import admin
from courses.models.course_model import Course, Learning, Prerequisite, Tag
from courses.models.video_model import Video
from courses.models.currency_model import CurrencyValue


class LearningAdmin(admin.TabularInline):
    model = Learning


class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite


class TagAdmin(admin.TabularInline):
    model = Tag


class VideoAdmin(admin.TabularInline):
    model = Video


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [LearningAdmin, PrerequisiteAdmin, TagAdmin, VideoAdmin]


class CurrencyValueAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbole', 'value')
    list_display_links = ('name', 'symbole', 'value')


admin.site.register(Video)
admin.site.register(CurrencyValue, CurrencyValueAdmin)
