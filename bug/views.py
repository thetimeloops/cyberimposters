from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import buginfo
# Create your views here.


@login_required(login_url='/login1')
def bug(request):
    mypost = buginfo.objects.all()
    return render(request,"bug.html",{'mypost':mypost})


@login_required(login_url='/login1')
def show(request,id):
    item = buginfo.objects.filter(post_id = id)[0]
    return render(request,"productpage.html",{'item':item})
