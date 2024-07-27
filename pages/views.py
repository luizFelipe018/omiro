from django.shortcuts import render

def home(request):
    return render(request, "pages/home.html", {})

def cashier(request):
    return render(request, "pages/cashier.html", {})

def stock(request):
    return render(request, "pages/stock.html", {})

# Create your views here.
