from django.db import models
import uuid
import os


class Document(models.Model):
    type = models.CharField(max_length=10)
    document = models.FileField(upload_to='media/')
    thumbnail = models.ImageField(upload_to='thumbnail_media/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

