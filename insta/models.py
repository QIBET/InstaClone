from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Image(models.Model):
    image_name =models.CharField(max_length =30)
    image_caption =models.CharField(max_length =50)
    image = models.ImageField(upload_to = 'images/',blank = True)
    comments = models.TextField(max_length=100)
    likes = models.PositiveIntegerField(default=0)
    user = models.ForeignKey('Profile', on_delete = models.CASCADE,null='True', blank=True)
    
    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    @classmethod
    def get_images(cls):
        all_pics=cls.objects.all()
        return all_pics

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
    @classmethod
    def get_profiles(cls):
        profiles=cls.objects.all()
        return profiles

class Follow(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')

    def _str_(self):
        return f'{self.follower} Follow'


    

    def _str_(self):
        return f'{self.user.name} Image'
""" class Comments(models.Model):
    comment = models.CharField(max_length=100,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ForeignKey(Image,on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    
    @classmethod
    def get_comments(cls,id):
        comments = cls.objects.filter(image__id=id)
        return comments
    
    def save_comment(self):
        self.save()
    
    def __str__(self):
        
        return self.comment """