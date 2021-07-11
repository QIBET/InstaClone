from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^image/$', views.image_upload,name='uploadImage'),
    

]