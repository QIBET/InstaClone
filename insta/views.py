from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Image,Profile,Follow
from .forms import ImageUploadForm, ImageProfileForm, CommentForm,UpdateImageForm,UserCreationForm,
from django.contrib.auth.models import User




from .email import send_welcome_email


# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    images = Image.get_images()
    users = User.objects.exclude(id=request.user.id)

    return render(request, 'index.html',{"images":images,"users":users})

def image_upload(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageUploadForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('home')
    else:
        form = ImageUploadForm()
        return render(request,'upload.html', {"form":form})