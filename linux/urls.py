from django.urls import path
from . import views

urlpatterns = [
    path('',views.linux,name="linux"),
    path('bloglinux',views.bloglinux,name="bloglinux")
]
