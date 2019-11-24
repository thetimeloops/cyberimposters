from django.urls import path

from . import views

urlpatterns=[
    path('',views.bug,name="bug"),
    path('show/<int:id>',views.show,name="show"),
]
