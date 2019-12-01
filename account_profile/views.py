from django.shortcuts import render
from main.models import exclusive
# Create your views here.

def userprofile(request):
    profile = exclusive.objects.filter(username=request.user.username)
    return render(request,"index2.html",{'profile':profile})
