from django.db import models
import uuid
import os




class Document(models.Model):
    document = models.FileField()
    thumbnail = models.FileField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

