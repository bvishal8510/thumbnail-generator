from django.shortcuts import render
from PIL import Image, ImageFilter, ImageOps
from django.shortcuts import render, redirect, get_object_or_404, reverse
from core.models import Document
from core.forms import DocumentForm
from django.core.files.images import ImageFile
from django.views import View
from django.core.files import File
import os
from django.core.files.uploadedfile import SimpleUploadedFile
import datetime
from io import BytesIO, StringIO
import cv2
import numpy as np


class GenerateThumbnailView(View):
    form_class = DocumentForm
    template_name = 'core/base.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self,request, *args, **kwargs):
            form = self.form_class(request.POST, request.FILES)
            if form.is_valid():
                type = ((dict(request.POST))['type'][0])
                form1 = form.save(commit=False)
                if type == 'image':
                    form1.document = dict(form.files)['files'][0]
                    form1.uploaded_at = datetime.datetime.now()
                elif type == 'audio':
                    form1.document = Image.open('core/static/images/audio.jpg')
                    form1.uploaded_at = datetime.datetime.now()
                elif type == 'text':
                    form1.document = Image.open('core/static/images/text.jpg')
                    form1.uploaded_at = datetime.datetime.now()
                elif type == 'video':
                    print("file",list(dict(form.files)['files'][0]))
                    cap = cv2.VideoCapture(str(dict(form.files)['files'][0]))
                    name = str(dict(form.files)['files'][0]) + "thumb" + ".jpg"
                    count = 0
                    while count < 14:
                      success, image = cap.read()
                      image1 = cv2.imwrite(name, image)     # save frame as JPEG file
                      count += 1
                    form1.document = image
                    form1.uploaded_at = datetime.datetime.now()
                form1.save()
                documents = Document.objects.all()
                return render(self.request, self.template_name, {'form': form, 'documents':documents})
            else:
                print("2")
                messages.error(self.request, "Data not valid.")
                form = self.form_class
                return render(self.request, self.template_name, {'form': form})



# data = form.cleaned_data['document']
                # print("data",data)
                # instance = form.save(commit=False)
                # filename = "thumb_"+str(instance.document)
                # im = Image.open(instance.document)
                # # StringIO(instance.document.read())
                # im.thumbnail((200, 200), Image.ANTIALIAS)
                # instance.uploaded_at = datetime.datetime.now()
                # print("Time",instance.uploaded_at)
                # im.save(filename, quality=60)
                # # image_file = ImageFile(im)
                # # instance.thumbnail = ImageClient(image=image_file)
                # # temp_handle = StringIO()
                # # im.save(temp_handle, PIL_TYPE)
                # # temp_handle.seek(0)
                # DJANGO_TYPE = 'image/jpeg'
                # suf = SimpleUploadedFile(os.path.split(instance.document.name)[-1],
                # im, content_type=DJANGO_TYPE)
                # instance.thumbnail = suf
                # print("instance1",instance.thumbnail)
                # instance.save()

# thumbnail = Image.open((dict(request.FILES))['document'][0]).thumbnail((200,200))
#                 .save("thumbnail_%s_%s" % (image, "_".join((200,200))))
#                 im = Image.open((dict(request.FILES))['document'][0])
#                 im.thumbnail((200, 200), Image.ANTIALIAS)
#                 im.save("T_" + str(uploaded_file), "JPEG")
#                 thumb_io = BytesIO()
#                 im.save(thumb_io, im.format, quality=60)
#                 ((dict(request.FILES))['document'][0]).save(im.filename, ContentFile(thumb_io.get_value()), save=False)