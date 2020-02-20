from django.shortcuts import render
from .models import linux_data
# Create your views here.
import nmap
import sys

def linux(request):
    mypost = linux_data.objects.all()
    return render(request,"linux.html",{'mypost':mypost})

def bloglinux(request,id):
    post = linux_data.objects.filter(post_id = id)[0]
    return render(request,"bloglinux.html",{'post':post})
