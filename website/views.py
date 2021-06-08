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



def core(request):
    return render(request, 'core.html',{})

def prvi(request):
    return render(request, 'core-program/prvi_program.html')

def drugi(request):
    return render(request, 'core-program/drugi_program.html')

def treci(request):
    return render(request, 'core-program/treci_program.html')

def cetvrti(request):
    return render(request, 'core-program/cetvrti_program.html')



def mass(request):
    return render(request, 'mass_gain.html')

def prvi_mass(request):
    return render(request, 'mass-gain/prvi_program_mass.html')

def drugi_mass(request):
    return render(request, 'mass-gain/drugi_program_mass.html')



