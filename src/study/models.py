from django.db import models
from django.utils import timezone
from django.contrib.messages import add_message

from Online_study.settings import MEDIA_ROOT, MEDIA_URL


import os


class Course(models.Model):
    title = models.CharField(max_length=200, unique=True)

    date = models.DateField(default=timezone.now())

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        os.mkdir(f'{MEDIA_ROOT}/{self.title}')
        super().save()

    def __str__(self):
        return f'<Course name: {self.title}>'


class Topic(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f'<Course name: {self.title}>'


class CourseVideo(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    path = models.FileField(upload_to='video')

    date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f'<Course name: {self.title}>'
