from django.shortcuts import render
from PIL import Image, ImageFilter, ImageOps
from django.shortcuts import render, redirect, get_object_or_404, reverse
from core.models import Document
from core.forms import DocumentForm
from django.views import View
from django.core.files import File
import os

class GenerateThumbnailView(View):
    form_class = DocumentForm
    template_name = 'core/base.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self,request, *args, **kwargs):
            form = self.form_class(request.POST, request.FILES)
            print(dict(request.FILES))
            print(form)
            if form.is_valid():
                return render(self.request, self.template_name, {'form': form})
            else:
                messages.error(self.request, "Data not valid.")
                form = self.form_class
                return render(self.request, self.template_name, {'form': form})
