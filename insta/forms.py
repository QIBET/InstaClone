from django import forms
from . models import Image,Profile

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['image_name','image_caption','comments','likes','user']
        
class ImageProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user',]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user','image',]