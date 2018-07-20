from django.db import models
import uuid
import os
from PIL import Image, ImageFilter, ImageOps
# from pytesser import *
from pytesseract import image_to_string
from django.core.files.images import ImageFile
from django.core.files import File
from django.core.files.uploadedfile import SimpleUploadedFile
import datetime
from io import BytesIO, StringIO
from django.core.files.base import ContentFile


class Document(models.Model):
    type = models.CharField(max_length=10)
    files = models.FileField(upload_to='media/')
    document = models.ImageField()
    thumbnail = models.ImageField(upload_to='thumbnail_media/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):

        if not self.make_thumbnail():
            # set to a default thumbnail
            raise Exception('Could not create thumbnail - is the file type valid?')

        super(Document, self).save(*args, **kwargs)

    def make_thumbnail(self):
        if self.type == 'audio':
            image = Image.open('core/static/images/audio.jpg')
            FTYPE = 'PNG'
            thumb_filename = (str(self.files).split("."))[0]+"_thumb"+'.png'
            print("file",self.files)
            print(thumb_filename)
        if self.type == 'text':
            image = Image.open('core/static/images/text.jpg')
            FTYPE = 'PNG'
            thumb_filename = (str(self.files).split("."))[0]+"_thumb"+'.png'
        else:
            image = Image.open(self.document)
            thumb_name, thumb_extension = os.path.splitext(self.document.name)
            thumb_extension = thumb_extension.lower()

            thumb_filename = thumb_name + '_thumb' + thumb_extension

            if thumb_extension in ['.jpg', '.jpeg']:
                FTYPE = 'JPEG'
            elif thumb_extension == '.gif':
                FTYPE = 'GIF'
            elif thumb_extension == '.png':
                FTYPE = 'PNG'
            else:
                return False    # Unrecognized file type
        image.thumbnail((200,200), Image.ANTIALIAS)

        # Save thumbnail to in-memory file as StringIO
        temp_thumb = BytesIO()
        image.save(temp_thumb, FTYPE)
        temp_thumb.seek(0)

        # set save=False, otherwise it will run in an infinite loop
        self.thumbnail.save(thumb_filename, ContentFile(temp_thumb.read()), save=False)
        temp_thumb.close()
        self.document = None

        return True

