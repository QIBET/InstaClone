from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Image,Profile,Follow



from .email import send_welcome_email


# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    images = Image.get_images()
    return render(request, 'index.html',{"images":images})

