from django.urls import path
from . import views 

urlpatterns = [
    path('',views.index, name = "index"),
    path('contact.html',views.contact, name = "contact"),
    path('about-us.html',views.about, name = "about-us"),
    path('blog.html',views.blog, name = "blog"),
    path('services.html',views.services, name = "services"),
    
    path('bmi-calculator.html',views.bmi, name = "bmi-calculator"),

    path('core.html',views.core, name = "core" ),
    path('prvi_program.html',views.prvi,name = "prvi_program"),
    path('drugi_program.html',views.drugi,name = "drugi_program"),
    path('treci_program.html',views.treci, name = "treci_program"),
    path('cetvrti_program.html',views.cetvrti, name = "cetvrti_program"),

    path('mass_gain.html',views.mass, name = "mass_gain"),
    path('prvi_program_mass.html',views.prvi_mass,name = "prvi_program_mass"),
    path('drugi_program_mass.html',views.drugi_mass,name = "drugi_program_mass"),

]
