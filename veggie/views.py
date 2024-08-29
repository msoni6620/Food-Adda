from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

def recipe(request):
    if(request.method=="POST"):
        data=request.POST
        recepie_image=request.FILES.get("recepie_image")
        recepie_name=data.get('recepie_name')
        recepie_description=data.get('recepie_description')
        Recepie.objects.create(
            recepie_image=recepie_image,
            recepie_name=recepie_name,
           recepie_description=recepie_description,
        )
        return redirect('/recipe/')
    # print(data)
    return render(request,"recepie.html", context={"page":"Recipe Hub"})
