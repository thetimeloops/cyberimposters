from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Blogspot , exclusive , notification
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
    if flag == "w0rld 1n s4fe h4nd5":
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
    count = notification.objects.all().count()
    return render(request,"main.html",{'count':count})

@login_required(login_url='/login1')
def blog(request):
    myposts = Blogspot.objects.all()
    return render(request, 'blog.html', {'myposts': myposts})

ctf_id=[]
@login_required(login_url='/login1')
def blogpost(request, id):
    post = Blogspot.objects.filter(post_id = id)[0]
    #info = exclusive.objects.filter(username=request.user)[0]
    info = exclusive.objects.get(username=request.user)
    if request.method == "POST":

        flag1 = request.POST.get('flag','')
        if(flag1 == post.flags):
            ctf_id.append(id)
            for i in range(len(ctf_id)):
                info.solvedctfid = ctf_id[i]
                info.save()
            curr_id = post.post_id
            print(info.solvedctfid)
            for i in ctf_id:
                if exclusive.objects.filter(solvedctfid=curr_id).exists():
                    return redirect('/')
            else:
                info.points = int(info.points) + int(post.points)
                info.save()
                return redirect("blog")
    return render(request,"blogspot.html",{'post':post})

login_required(login_url='/login1')
def alerts(request):
    noti = notification.objects.all()
    count = notification.objects.all().count()
    return render(request,"alert.html",{'noti':noti})


@login_required(login_url='/login1')
def logout(request):
    auth.logout(request)
    return redirect("/")



@login_required(login_url='/login1')
def profile(request):
    myposts = exclusive.objects.all()
    return render(request,"profile.html",{'myposts':myposts})
