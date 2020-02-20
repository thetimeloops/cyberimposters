from django.urls import path
from . import views

urlpatterns = [
    path('',views.crypto,name="crypto"),
    path('blogcrypto/<int:id>',views.blogcrypto,name="blogcrypto")

]
