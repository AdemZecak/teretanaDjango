from django.shortcuts import render

#glavni linkovi iz navbara

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

#linkovi iz menija za vjezbe (trbuh)

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

#linkovi iz menija za vjezbe (masa)

def mass(request):
    return render(request, 'mass_gain.html')

def prvi_mass(request):
    return render(request, 'mass-gain/prvi_program_mass.html')

def drugi_mass(request):
    return render(request, 'mass-gain/drugi_program_mass.html')


#linkovi iz menija za vjezbe (definicija)

def definicija(request):
    return render(request, 'definicija.html')

def prvi_definicija(request):
    return render(request, 'definicija-program/prvi_program_definicija.html')

def drugi_definicija(request):
    return render(request, 'definicija-program/drugi_program_definicija.html')

def treci_definicija(request):
    return render(request, 'definicija-program/treci_program_definicija.html')


#linkovi iz menija za vjezbe(trening snage)


def snaga(request):
    return render(request, 'snaga.html')

def program_snaga(request):
    return render(request, 'snaga-program/program_snaga.html')


#yoga 

def yoga(request):
    return render(request, 'yoga.html')

def program_yoga(request):
    return render(request, 'yoga-program/program_yoga.html')


