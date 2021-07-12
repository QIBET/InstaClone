from django.conf.urls import url
from . import views

urlpatterns=[
    url('',views.home,name = 'home'),
    url(r'^image/$', views.image_upload,name='uploadImage'),
    url(r'^profile/$', views.profile,name='profile'),
    url(r'^edit/$',views.profile_edit,name='edit'),
    url(r'^user/$',views.search_user,name='search'),

]