from django.shortcuts import render

def home_view(request):
    return render(request, "index.html")

def contact(request):
    return render(request, "contact.html")

def jewelry(request):
    return render(request,"Jewelry.html")

def portrait(request):
    return render(request,"Portrait.html")

def marriage(request):
    return render(request,"Marriage.html")

def birthday(request):
    return render(request,"Birthday.html")

def pre(request):
    return render(request,"Pre-Wedding.html")

def clothing(request):
    return render(request,"Clothing.html")

def auto(request):
    return render(request,"Auto-Mobile.html")

def business(request):
    return render(request,"Business.html")

def frames(request):
    return render(request,"Frames.html")

def privacy(request):
    return render(request,"privacy.html")

def refund(request):
    return render(request,"refund.html")