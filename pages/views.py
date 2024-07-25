from django.shortcuts import render

def home(request):
    return render(request, "pages/home.html", {})

def cashier(request):
    return render(request, "pages/cashier.html", {})

# Create your views here.
