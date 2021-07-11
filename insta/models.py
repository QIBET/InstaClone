from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Image(models.Model):
    image_name =models.CharField(max_length =30)
    image_caption =models.CharField(max_length =50)
    image = models.ImageField(upload_to = 'images/',blank = True)
    comments = models.TextField(max_length=100)
    user = models.ForeignKey('Profile', on_delete = models.CASCADE,null='True', blank=True)
    likes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profilepics/',blank = True,)
    bio = models.TextField(max_length=100)
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.profile_photo

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

class Follow(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')

    def _str_(self):
        return f'{self.follower} Follow'


    

    def _str_(self):
        return f'{self.user.name} Image'