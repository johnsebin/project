from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(reguest):

    return render(reguest,"home.html")
def about(request):
    return render(request,"about.html")
def contacts(request):
    return render(request,"contact.html")
def details(request):
    return render(request,"details.html")
def thanks(request):
    return render(request,"thanks.html")



# Create your views here.
