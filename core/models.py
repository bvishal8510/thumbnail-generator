from django.db import models
import uuid
import os


class Document(models.Model):
    document = models.FileField(upload_to='media')
    thumbnail = models.ImageField(upload_to='media')
    uploaded_at = models.DateTimeField(auto_now_add=True)

