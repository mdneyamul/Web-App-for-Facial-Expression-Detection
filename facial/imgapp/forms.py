from django import forms
from .models import *

class ImageUpForm(forms.ModelForm):

    class Meta:
        model = ImageUp
        fields = ['up_img']
    