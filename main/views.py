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

    if request.method == "POST":
        point_temp =0
        flag1 = request.POST.get('flag','')
        if(flag1 == post.flags):
            point = exclusive.objects.update(points= point_temp+10)

            return redirect("blog")
        else:
            return render(request, 'blogspot.html', {'post':post})
    return render(request, 'blogspot.html', {'post':post})

@login_required(login_url='/login1')
def search(request):
    query = request.GET.get('search_query')
    search_fields = ['^title','habody','body']
    posts = Blogspot.objects.filter(search_filter(search_fields, query))
    return render(request,"search.html",{'myposts':myposts})

@login_required(login_url='/login1')
def profile(request):
    myposts = exclusive.objects.all()
    return render(request,"profile.html",{'myposts':myposts})

@login_required(login_url='/login1')
def ctfpage(request):
    pass


@login_required(login_url='/login1')
def check_flag_blog(request):

    flag1 = request.POST.get('flag','')
    check_flag_var = Blogspot.objects.filter(post_id=id)
    print(check_flag_var.flags)
    if Blogspot.objects.filter(flags = flag1).exists():
        flagfound=True
        return render(request,"blog.html",flagfound)
    else:

        return HttpResponse("<script>alert('try AGain')</script>")
