from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Blogspot , exclusive
from django.contrib.auth.models import User , auth
from django.contrib import auth
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request,"index.html")

@login_required(login_url='/login1')
def check_flag(request):
    flag = request.POST.get('flag')
    if flag == "^FLAG^as&97ejldsjfjlsdjlkfaklkasd$":
        return render(request,"exclusive.html")
    else:
        return redirect("/")

@login_required(login_url='/login1')
def ctf(request):
    return render(request,"ctf.html")

def login1(request):
    if request.method=="POST":
        username = request.POST.get('username1','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request,user)

            return redirect("main")
        else:
            err= "Invalid Username or Password"
            return render(request,"login1.html",{'err':err})
    else:
        return render(request,"login1.html")


def signup(request):
    if request.method=="POST":
        username = request.POST.get('username','')
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        password = request.POST.get('password','')
        password1 = request.POST.get('password1','')
        gender = request.POST.get('gender','')
        phone = request.POST.get('number','')

        if password == password1:
            if User.objects.filter(email=email).exists():
                err = "Email Already exists"
                return render(request,"sign_up.html",{'err':err})
            elif User.objects.filter(username=username).exists():
                err = "Username Taken"
                return render(request,"sign_up.html",{'err':err})

            else:
                user_main = User.objects.create_user(username=username,password=password,email=email,first_name=name)
                user_main.save()
                user  =  exclusive(username=username ,name=name, email=email ,gender=gender , phone=phone,password=password)
                user.save()
                return redirect("login1")
    return render(request,"sign_up.html")

@login_required(login_url='/login1')
def main(request):
    myposts = exclusive.objects.all()
    return render(request,"main.html",{'myposts':myposts})

@login_required(login_url='/login1')
def blog(request):
    myposts = Blogspot.objects.all()
    return render(request, 'blog.html', {'myposts': myposts})

@login_required(login_url='/login1')
def blogpost(request, id):
    post = Blogspot.objects.filter(post_id = id)[0]
    #info = exclusive.objects.filter(username=request.user)[0]
    info = exclusive.objects.get(username=request.user)
    if request.method == "POST":
        flag1 = request.POST.get('flag','')
        if(flag1 == post.flags):
            info.points = int(info.points) + 10
            info.save()
            post.is_solved=True
            post.save()
            return redirect(blog)
        else:
            return render(request, 'blogspot.html', {'post':post})
    return render(request, 'blogspot.html', {'post':post})



@login_required(login_url='/login1')
def profile(request):
    myposts = exclusive.objects.all()
    return render(request,"profile.html",{'myposts':myposts})
