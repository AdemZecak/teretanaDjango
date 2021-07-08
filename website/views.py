from website.models import Prvi_program_ponedjeljak
from django.shortcuts import render
from .models import Cetvrti_program_cetvrtak, Cetvrti_program_petak, Cetvrti_program_ponedjeljak, Cetvrti_program_srijeda, Cetvrti_program_subota, Cetvrti_program_utorak, Drugi_program_cetvrtak, Drugi_program_petak, Drugi_program_ponedjeljak, Drugi_program_srijeda, Drugi_program_subota, Drugi_program_utorak, Misicna_definicija2_petak, Misicna_definicija2_ponedjeljak, Misicna_definicija3_nedjelja, Misicna_definicija3_petak, Misicna_definicija3_ponedjeljak, Misicna_definicija_petak, Misicna_definicija_ponedjeljak, Misicna_definicija_srijeda, Misicna_definicija_srijeda2, Misicna_definicija_srijeda3, Placanje, Program_mass2_cetvrtak, Program_mass2_petak, Program_mass2_ponedjeljak, Program_mass2_utorak, Program_mass_cetvrtak, Program_mass_petak, Program_mass_ponedjeljak, Program_mass_utorak, Program_snaga_petak, Program_snaga_ponedjeljak, Program_snaga_srijeda, Program_yoga, Prvi_program_cetvrtak, Prvi_program_petak, Prvi_program_ponedjeljak, Prvi_program_srijeda, Prvi_program_subota, Prvi_program_utorak, Treci_program_cetvrtak, Treci_program_petak, Treci_program_ponedjeljak, Treci_program_srijeda, Treci_program_subota, Treci_program_utorak


#glavni linkovi iz navbara
#opcija za plaćanje
def index(request):
    
    placanje = Placanje.objects.all()
    return render(request, 'index.html', {'placanje': placanje})





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

    ponedjeljak = Prvi_program_ponedjeljak.objects.all()
    utorak = Prvi_program_utorak.objects.all()
    srijeda = Prvi_program_srijeda.objects.all()
    cetvrtak = Prvi_program_cetvrtak.objects.all()
    petak = Prvi_program_petak.objects.all()
    subota = Prvi_program_subota.objects.all()

    context = {'ponedjeljak': ponedjeljak, 'utorak':utorak,'srijeda':srijeda,'cetvrtak':cetvrtak,'petak':petak,'subota':subota}

    
    return render(request, 'core-program/prvi_program.html', context)

  


def drugi(request):
    ponedjeljak = Drugi_program_ponedjeljak.objects.all()
    utorak = Drugi_program_utorak.objects.all()
    srijeda = Drugi_program_srijeda.objects.all()
    cetvrtak = Drugi_program_cetvrtak.objects.all()
    petak = Drugi_program_petak.objects.all()
    subota = Drugi_program_subota.objects.all()

    context = {'ponedjeljak': ponedjeljak, 'utorak':utorak,'srijeda':srijeda,'cetvrtak':cetvrtak,'petak':petak,'subota':subota}

    
    return render(request, 'core-program/drugi_program.html', context)






def treci(request):
    ponedjeljak = Treci_program_ponedjeljak.objects.all()
    utorak = Treci_program_utorak.objects.all()
    srijeda = Treci_program_srijeda.objects.all()
    cetvrtak = Treci_program_cetvrtak.objects.all()
    petak = Treci_program_petak.objects.all()
    subota = Treci_program_subota.objects.all()

    context = {'ponedjeljak': ponedjeljak, 'utorak':utorak,'srijeda':srijeda,'cetvrtak':cetvrtak,'petak':petak,'subota':subota}

    
    return render(request, 'core-program/treci_program.html', context)

def cetvrti(request):
    ponedjeljak = Cetvrti_program_ponedjeljak.objects.all()
    utorak = Cetvrti_program_utorak.objects.all()
    srijeda = Cetvrti_program_srijeda.objects.all()
    cetvrtak = Cetvrti_program_cetvrtak.objects.all()
    petak = Cetvrti_program_petak.objects.all()
    subota = Cetvrti_program_subota.objects.all()

    context = {'ponedjeljak': ponedjeljak, 'utorak':utorak,'srijeda':srijeda,'cetvrtak':cetvrtak,'petak':petak,'subota':subota}

    
    return render(request, 'core-program/cetvrti_program.html', context)




#linkovi iz menija za vjezbe (masa)

def mass(request):
    return render(request, 'mass_gain.html')

def prvi_mass(request):

    ponedjeljak = Program_mass_ponedjeljak.objects.all()
    utorak = Program_mass_utorak.objects.all()
    cetvrtak = Program_mass_cetvrtak.objects.all()
    petak = Program_mass_petak.objects.all()


    context = {'ponedjeljak': ponedjeljak, 'utorak':utorak,'cetvrtak':cetvrtak,'petak':petak}

    
    return render(request, 'mass-gain/prvi_program_mass.html', context)

def drugi_mass(request):
    ponedjeljak = Program_mass2_ponedjeljak.objects.all()
    utorak = Program_mass2_utorak.objects.all()
    cetvrtak = Program_mass2_cetvrtak.objects.all()
    petak = Program_mass2_petak.objects.all()


    context = {'ponedjeljak': ponedjeljak, 'utorak':utorak,'cetvrtak':cetvrtak,'petak':petak}

    
    return render(request, 'mass-gain/drugi_program_mass.html', context)


#linkovi iz menija za vjezbe (definicija)



def definicija(request):
    return render(request, 'definicija.html')



def prvi_definicija(request):

    ponedjeljak = Misicna_definicija_ponedjeljak.objects.all()
    srijeda = Misicna_definicija_srijeda.objects.all()
    petak = Misicna_definicija_petak.objects.all()

    context = {'ponedjeljak': ponedjeljak, 'srijeda':srijeda,'petak':petak}
    
    return render(request, 'definicija-program/prvi_program_definicija.html',context)




def drugi_definicija(request):

    ponedjeljak = Misicna_definicija2_ponedjeljak.objects.all()
    srijeda = Misicna_definicija_srijeda2.objects.all()
    petak = Misicna_definicija2_petak.objects.all()

    context = {'ponedjeljak': ponedjeljak, 'srijeda':srijeda,'petak':petak}
    
    return render(request, 'definicija-program/drugi_program_definicija.html',context)

def treci_definicija(request):

    ponedjeljak = Misicna_definicija3_ponedjeljak.objects.all()
    srijeda = Misicna_definicija_srijeda3.objects.all()
    petak = Misicna_definicija3_petak.objects.all()
    nedjelja = Misicna_definicija3_nedjelja.objects.all()

    context = {'ponedjeljak': ponedjeljak, 'srijeda':srijeda,'petak':petak,'nedjelja':nedjelja}

    return render(request, 'definicija-program/treci_program_definicija.html',context)


#linkovi iz menija za vjezbe(trening snage)

#######PROGRAM SNAGA#################



def snaga(request):
    return render(request, 'snaga.html')

def program_snaga(request):
    ponedjeljak = Program_snaga_ponedjeljak.objects.all()
    srijeda = Program_snaga_srijeda.objects.all()
    petak = Program_snaga_petak.objects.all()

    context = {'ponedjeljak': ponedjeljak, 'srijeda':srijeda,'petak':petak}

    return render(request, 'snaga-program/program_snaga.html',context)


#yoga 

def yoga(request):
    return render(request, 'yoga.html')

def program_yoga(request):

    yoga = Program_yoga.objects.all()

    context = {'yoga': yoga}

    return render(request, 'yoga-program/program_yoga.html', context)






#plaćanje



