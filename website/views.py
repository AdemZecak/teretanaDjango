from django.shortcuts import render



def index(request):
    return render(request, 'index.html',{})

def register(request):
    return render(request,'register.html',{})

def contact(request):
    return render(request, 'contact.html',{})

def about(request):
    return render(request, 'about-us.html',{})

def blog(request):
    return render(request, 'blog.html',{})

def services(request):
    return render(request, 'services.html',{})

def bmi(request):
    return render(request, 'bmi-calculator.html',{})



