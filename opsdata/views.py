from .models import  Flight_Detail, Flight_Movement
from django.shortcuts import render

def statistics(request):
    details = Flight_Detail.objects.filter()
    movements = Flight_Movement.objects.filter()
    context = {

        "details": details,
        "movements": movements,
    }
    return render(request,'test.html',context)