from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Follow, Image, Profile

admin.site.register(Image)
admin.site.register(Profile)
admin.site.register(Follow)