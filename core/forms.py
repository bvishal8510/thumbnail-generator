from django import forms
from core.models import Document

choices = (('image','Image'),('text','Text'),('audio','Audio'),('video','Video'))

class DocumentForm(forms.ModelForm):                                                       # it is connected to Document table in database
    type = forms.ChoiceField(choices=choices,label="File type", widget=forms.Select() )
    # thumbnail = forms.ImageField()
    # uploaded_at = forms.DateTimeField()

    class Meta:
        model = Document
        fields = ('document','type')