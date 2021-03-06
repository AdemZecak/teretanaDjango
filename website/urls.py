from django.urls import path
from . import views
import website 



urlpatterns = [

    #BMI
    path('bmi-calculator.html',views.bmi, name = "bmi-calculator"),
    path('racun',views.racun, name = "racun"),
    ######


    #checkbox save btn

    path('cross_off/<list_id>',views.cross_off,name = "cross_off"),
    path('uncross/<list_id>',views.uncross,name = "uncross"),
    path('edit/<list_id>',views.edit,name="edit"),
    #################
    
    path('contact.html',views.contact, name = "contact"),
    path('about-us.html',views.about, name = "about-us"),
    path('blog.html',views.blog, name = "blog"),
    path('services.html',views.services, name = "services"),

    #LOGIN I REGISTRACIJA
    path('login-registracija.html',views.loginRegistracija, name = "loginRegistracija"),
    
    #vjezbe za trbuh
    path('core.html',views.core, name = "core" ),
    path('prvi_program.html',views.prvi,name = "prvi_program"),
    path('drugi_program.html',views.drugi,name = "drugi_program"),
    path('treci_program.html',views.treci, name = "treci_program"),
    path('cetvrti_program.html',views.cetvrti, name = "cetvrti_program"),
    #vjezbe za dobijanje mase
    path('mass_gain.html',views.mass, name = "mass_gain"),
    path('prvi_program_mass.html',views.prvi_mass,name = "prvi_program_mass"),
    path('drugi_program_mass.html',views.drugi_mass,name = "drugi_program_mass"),
    #vjezbe za definicije
    path('definicija.html',views.definicija, name = "definicija"),
    path('prvi_program_definicija.html',views.prvi_definicija,name = "prvi_program_definicija"),
    path('drugi_program_definicija.html',views.drugi_definicija,name = "drugi_program_definicija"),
    path('treci_program_definicija.html',views.treci_definicija,name = "treci_program_definicija"),

    #vježbe snage

    path('snaga.html',views.snaga, name = "snaga"),
    path('program_snaga.html',views.program_snaga, name = "program_snaga"),

    #yoga

    path('yoga.html',views.yoga, name = "yoga"),
    path('program_yoga.html',views.program_yoga, name = "program_yoga"),




    #plaćanje checkout

    path('simple-checkout.html',views.simpleCheckout, name = "simple-checkout"),
    
    path('',views.index, name = "index"),


    
    path('checkout/<int:pk>/', views.checkout, name="checkout"), 
    path('complete/', views.paymentComplete, name="complete"),

  

    

    

]
