from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import blog

@login_required(login_url='/login1')
def crypto(request):
    all = blog.objects.all()
    return render(request,"c.html",{'all':all})

def blogcrypto(request,id):
    single = blog.objects.filter(post_id=id)[0]
    return render(request,"single.html",{'single':single})
