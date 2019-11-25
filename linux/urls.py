from django.urls import path
from . import views

urlpatterns = [
    path('',views.linux,name="linux"),
    path('bloglinux/<int:id>',views.bloglinux,name="bloglinux")
]
