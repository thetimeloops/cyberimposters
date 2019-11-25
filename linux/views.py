from django.shortcuts import render

# Create your views here.


def linux(request):
    return render(request,"linux.html")

def bloglinux(request):
    return render(request,"bloglinux.html")
