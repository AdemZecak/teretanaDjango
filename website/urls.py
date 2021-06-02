from django.urls import path
from . import views 

urlpatterns = [
    path('',views.index, name = "index"),
    path('contact.html',views.contact, name = "contact"),
    path('about-us.html',views.about, name = "about-us"),
    path('blog.html',views.blog, name = "blog"),
    path('services.html',views.services, name = "services"),
    path('bmi-calculator.html',views.bmi, name = "bmi-calculator"),
]
