from django.shortcuts import render
from PIL import Image, ImageFilter, ImageOps
from django.shortcuts import render, redirect, get_object_or_404, reverse
from core.models import Document
from core.forms import DocumentForm
from django.views import View
from django.core.files import File
import os
import datetime
from io import BytesIO

class GenerateThumbnailView(View):
    form_class = DocumentForm
    template_name = 'core/base.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self,request, *args, **kwargs):
            form = self.form_class(request.POST, request.FILES)
            uploaded_file = (dict(request.FILES))['document'][0]
            print(form)
            if form.is_valid():
                print("1")
                # thumbnail = Image.open((dict(request.FILES))['document'][0]).thumbnail((200,200))
                # .save("thumbnail_%s_%s" % (image, "_".join((200,200))))
                im = Image.open((dict(request.FILES))['document'][0])
                im.thumbnail((200, 200), Image.ANTIALIAS)
                # im.save("T_" + str(uploaded_file), "JPEG")
                thumb_io = BytesIO()
                im.save(thumb_io, im.format, quality=60)
                # ((dict(request.FILES))['document'][0]).save(im.filename, ContentFile(thumb_io.get_value()), save=False)
                Document.objects.create(document=(dict(request.FILES))['document'][0], thumbnail=im, uploaded_at=datetime.datetime.now())
                return render(self.request, self.template_name, {'form': form,'image':im})
            else:
                print("2")
                messages.error(self.request, "Data not valid.")
                form = self.form_class
                return render(self.request, self.template_name, {'form': form})
