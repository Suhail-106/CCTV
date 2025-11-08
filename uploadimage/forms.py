from django import forms
from .models import ImageURL

class ImageURLForm(forms.ModelForm):
    class Meta:
        model = ImageURL
        fields = ['url']
