from django import forms
from core.models import Document

class DocumentForm(forms.ModelForm):                                                       # it is connected to Document table in database
    
    class Meta:
        model = Document
        fields = ('document',)