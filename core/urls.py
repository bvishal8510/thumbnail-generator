from django.conf.urls import url, include
from core.views import GenerateThumbnailView

urlpatterns = [

    url(r'^$', GenerateThumbnailView.as_view(), name='thumbnail'),
   ]