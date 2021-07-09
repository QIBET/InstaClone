from django.db import models

# Create your models here.
class Image(models.Model):
    image_name =models.CharField(max_length =30)
    image_caption =models.CharField(max_length =50)
    image = models.ImageField(upload_to = 'images/',blank = True)
    profile = models.ForeignKey('Profile', on_delete = models.CASCADE,null='True', blank=True)
    comments = models.TextField(max_length=100)
    likes = models.Value(default = 0)
