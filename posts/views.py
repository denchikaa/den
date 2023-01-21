from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.




def index(request):
    context = {
        "title": "Главная страница",
    }
    return render(request, "index.html", context=None)

def about(request):
    context = {
        "title": "О нас",
    }    
    return render(request, "about.html", context)

def contact(request):
    context = {
        "title": "Контакты",
    }

    return render(request, "contacts.html", context)

