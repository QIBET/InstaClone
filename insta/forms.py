from django import forms
from django.db.models import fields
from . models import Comments, Image,Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile','comments','likes','user']
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['image','date_posted','user']

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
class UpdateImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['comments','likes','user']
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user',]
