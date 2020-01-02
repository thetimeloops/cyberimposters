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
    path("check_flag",views.check_flag,name="check_flag"),
    path('profile',views.profile,name="profile"),
    path('alerts',views.alerts,name="alert"),
    path('logout',views.logout,name="logout")

]
