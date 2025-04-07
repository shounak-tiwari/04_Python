from django.shortcuts import render

from .models import Product


# Create your views here.

def HomePage(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')


def signup(request):
    return render(request,'signup.html')

from django.http import HttpResponse


def stafflogin(request):

    if request.method =="POST":
        name  = request.POST.get('productname')
        price = request.POST.get('productprice')
        quantity = request.POST.get('productquantity')

        temp = Product(name=name,price=price,quantity=quantity)

        temp.save()

        return HttpResponse("data has been saved in database ")


    return render(request,'stafflogin.html')