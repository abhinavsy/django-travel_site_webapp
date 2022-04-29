from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from travelapp.models import Place, Team


def demo(request):
    obj=Place.objects.all()
    team=Team.objects.all()
    return render(request,"index.html",{'result':obj,'result2':team})


# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request,"about.html",{'result':res})

