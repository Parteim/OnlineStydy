from django.contrib import admin

from .models import Course, CourseVideo, Topic

admin.site.register(Course)
admin.site.register(CourseVideo)
admin.site.register(Topic)
