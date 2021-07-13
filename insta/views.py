from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Image,Profile,Comments
from .forms import ImageUploadForm, CommentForm, ProfileForm,UserCreationForm
from django.contrib.auth.models import User
from vote.managers import  VotableManager
votes = VotableManager()





from .email import send_welcome_email


# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    images = Image.objects.all()
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
def profile(request):
    
    current_user=request.user
    profile= Profile.objects.filter(user=current_user).first()
    posts =  request.user.image_set.all()
    
    
    
    return render(request,'profile.html',{"images":posts,"profile":profile,"current_user":current_user})
        
def profile_edit(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('profile')

    else:
        form = ProfileForm()
        return render(request,'edit_profile.html',{"form":form})

def search_user(request):
    
    if 'search_user' in request.GET and request.GET["search_user"]:

        search_term = request.GET.get("search_user")
        searched_user = User.objects.filter(username__icontains=search_term)
        message = f"{search_term}"  
        return render(request, 'search.html', {"message": message, "users": searched_user})

    else:
        message = "You haven't searched for any term "
        return render(request, 'search.html', {"message": message})
def add_comment(request,id):

    current_user = request.user
    image = Image.get_single_photo(id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        print(form)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.image_id = id
            comment.save()
        return redirect('home')

    else:
        form = CommentForm()
        return render(request,'insta/new_comment.html',{"form":form,"image":image})  
    
def comments(request,id):
    comments = Comments.get_comments(id)
    number = len(comments   )
    
    return render(request,'insta/comments.html',{"comments":comments,"number":number})        

@login_required (login_url='/accounts/register/')          
def like_images(request,id):
    image =  Image.get_single_photo(id)
    user = request.user
    user_id = user.id
    
    if user.is_authenticated:
        uplike = image.votes.up(user_id)
        image.likes = image.votes.count()
        image.save()
        
    return redirect('home')