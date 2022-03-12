from django.http import HttpResponse
from django.shortcuts import render 
# from django.randere import render
def home_page(request):
    context = {"title":"Hello From other side"}
    return render(request, 'home.html',context)

def contact_page(request):
    context = {"title":"Hello From Contact side"}

    return render(request, 'contact.html',context)

def about_page(request):
    return HttpResponse("<h1>About us</h1>")
