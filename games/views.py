from django.shortcuts import render
from .models import game_regis , about_game
# Create your views here.

def index(request):
    games = about_game.objects.all()
    return render(request,"games.html",{'games':games})


def regis(request):
    if request.method=="POST":
        name = request.POST.get('name','')
        phone = request.POST.get('phone','')
        team_type = request.POST.get('type_team','')
        year  = request.POST.get('year_game','')
        email = request.POST.get('email','')

        if game_regis.objects.filter(email=email).exists():
            suc = "Email Already Registered"
            return render(request,"regis.html",{'suc':suc})
        elif game_regis.objects.filter(phone=phone).exists():
            suc = "Phone Number already taken"
            return render(request,"regis.html",{'suc':suc})
        else:
            game_save = game_regis(name=name,phone=phone,type=team_type,year = year,email=email)
            game_save.save()
            suc = "Succesfully Registered"
            return render(request,"regis.html",{'suc':suc})
    return render(request,"regis.html")
