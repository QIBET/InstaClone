from django.db import models

# Create your models here.
class Image(models.Model):
    image_name =models.CharField(max_length =30)
    image_caption =models.CharField(max_length =50)
    image = models.ImageField(upload_to = 'images/',blank = True)
    comments = models.TextField(max_length=100)
    likes = models.PositiveBigIntegerField(default = 0)
    profile = models.ForeignKey('Profile', on_delete = models.CASCADE,null='True', blank=True)


    def __str__(self):
        return self.image_name

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'images/',blank = True)
    bio = models.TextField(max_length=100)

    def __str__(self):
        return self.profile_photo