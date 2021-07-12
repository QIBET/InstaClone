from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^image/$', views.image_upload,name='uploadImage'),
    url(r'^profile/$', views.profile,name='profile'),
    url(r'^edit/$',views.profile_edit,name='edit'),
    url(r'^user/$',views.search_user,name='search'),
     url(r'^new_comment/(\d+)/$' ,views.add_comment,name='newComment'),
    url(r'^comment/(\d+)/$' ,views.comments,name='comments'),
    url(r'^likes/(\d+)/$' , views.like_images, name='likes')
]