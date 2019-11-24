from django.urls import path
from main import views

urlpatterns = [
    path('',views.index,name="index"),
    path('ctf',views.ctf,name="ctf"),
    path('login1',views.login1,name="login1"),
    path('signup',views.signup,name="signup"),
    path('main',views.main,name="main"),
    path('blog',views.blog,name="blog"),
    path("blogpost/<int:id>", views.blogpost, name="blogHome"),
    path("search",views.blog,name="search"),
    path("check_flag",views.check_flag,name="check_flag"),
    path('profile',views.profile,name="profile"),
    path('ctfpage',views.ctfpage,name="ctfpage"),
    path('blogpost/check_flag_blog/',views.check_flag_blog,name="check_flag_blog"),


]
