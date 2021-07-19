from django.contrib.auth.models import User
from django.db import models 
from django.contrib.auth.models import User 
#session



#trbušni zid 


#ponedjeljak PRVI PROGRAM

class Prvi_program_ponedjeljak(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/ponedjeljak' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)
    completed = models.BooleanField(default=False)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja
        return self.completed


    class Meta:
        verbose_name_plural = "Prvi_program_ponedjeljak"

#utorak

class Prvi_program_utorak(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/utorak' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Prvi_program_utorak"



#srijeda

class Prvi_program_srijeda(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/srijeda' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Prvi_program_srijeda"


#cetvrtak

class Prvi_program_cetvrtak(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/cetvrtak' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Prvi_program_cetvrtak"



#petak

class Prvi_program_petak(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/petak' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Prvi_program_petak"

#subota 

class Prvi_program_subota(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/subota' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Prvi_program_subota"





#ponedjeljak DRUGI PROGRAM 

class Drugi_program_ponedjeljak(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/ponedjeljak' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Drugi_program_ponedjeljak"

#utorak

class Drugi_program_utorak(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/utorak' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Drugi_program_utorak"



#srijeda

class Drugi_program_srijeda(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/srijeda' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Drugi_program_srijeda"


#cetvrtak

class Drugi_program_cetvrtak(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/cetvrtak' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Drugi_program_cetvrtak"



#petak

class Drugi_program_petak(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/petak' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Drugi_program_petak"

#subota 

class Drugi_program_subota(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/subota' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Drugi_program_subota"




#ponedjeljak TREĆI PROGRAM ##########################################################

class Treci_program_ponedjeljak(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/ponedjeljak' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Treci_program_ponedjeljak"

#utorak

class Treci_program_utorak(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/utorak' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Treci_program_utorak"



#srijeda

class Treci_program_srijeda(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/srijeda' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Treci_program_srijeda"


#cetvrtak

class Treci_program_cetvrtak(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/cetvrtak' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Treci_program_cetvrtak"



#petak

class Treci_program_petak(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/petak' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Treci_program_petak"

#subota 

class Treci_program_subota(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/subota' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Treci_program_subota"




#ponedjeljak TREĆI PROGRAM ##########################################################

class Cetvrti_program_ponedjeljak(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/ponedjeljak' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Cetvrti_program_ponedjeljak"

#utorak

class Cetvrti_program_utorak(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/utorak' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Cetvrti_program_utorak"



#srijeda

class Cetvrti_program_srijeda(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/srijeda' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Cetvrti_program_srijeda"


#cetvrtak

class Cetvrti_program_cetvrtak(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/cetvrtak' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Cetvrti_program_cetvrtak"



#petak

class Cetvrti_program_petak(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/petak' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Cetvrti_program_petak"

#subota 

class Cetvrti_program_subota(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/subota' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Cetvrti_program_subota"


##############YOGA PROGRAM#############################

class Program_yoga(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/yoga' )
    vjezbe = models.CharField(max_length=200)
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Program_yoga"



#####################################################################################



#POVEĆANJE MIŠIĆNE MASE (MASS GAIN)




class Program_mass_ponedjeljak(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/mass/ponedjeljak' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Program_mass_ponedjeljak"

#utorak

class Program_mass_utorak(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/mass/utorak' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Program_mass_utorak"


#cetvrtak

class Program_mass_cetvrtak(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/mass/cetvrtak' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Program_mass_cetvrtak"



#petak

class Program_mass_petak(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/mass/petak' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Program_mass_petak"





#################################################################################




#POVEĆANJE MIŠIĆNE MASE 2(MASS GAIN)




class Program_mass2_ponedjeljak(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/mass/ponedjeljak' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Program_mass2_ponedjeljak"

#utorak

class Program_mass2_utorak(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/mass/utorak' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Program_mass2_utorak"


#cetvrtak

class Program_mass2_cetvrtak(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/mass/cetvrtak' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Program_mass2_cetvrtak"



#petak

class Program_mass2_petak(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/mass/petak' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Program_mass2_petak"



###################PROGRAM SNAGA#################################################


class Program_snaga_ponedjeljak(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/snaga/ponedjeljak' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Program_snaga_ponedjeljak"

#srijeda

class Program_snaga_srijeda(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/snaga/srijeda' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Program_snaga_srijeda"


#petak

class Program_snaga_petak(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/snaga/petak' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Program_snaga_petak"



#################################################################################




################### PROGRAM DEFINICIJA #################################################


class Misicna_definicija_ponedjeljak(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/definicija/ponedjeljak' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Misicna_definicija_ponedjeljak"

#srijeda

class Misicna_definicija_srijeda(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/definicija/srijeda' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Misicna_definicija_srijeda"


#petak

class Misicna_definicija_petak(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/definicija/petak' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Misicna_definicija_petak"



#################################################################################




################### PROGRAM DEFINICIJA 2 #################################################


class Misicna_definicija2_ponedjeljak(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/definicija2/ponedjeljak' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Misicna_definicija2_ponedjeljak"

#srijeda

class Misicna_definicija_srijeda2(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/definicija2/srijeda' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Misicna_definicija2_srijeda"


#petak

class Misicna_definicija2_petak(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/definicija2/petak' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Misicna_definicija2_petak"



#################################################################################



################### PROGRAM DEFINICIJA 3 #################################################


class Misicna_definicija3_ponedjeljak(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/definicija3/ponedjeljak' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Misicna_definicija3_ponedjeljak"

#srijeda

class Misicna_definicija_srijeda3(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/definicija3/srijeda' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Misicna_definicija3_srijeda"


#petak

class Misicna_definicija3_petak(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/definicija3/petak' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Misicna_definicija3_petak"


#NEDJELJA

class Misicna_definicija3_nedjelja(models.Model):
    gif = models.ImageField(null = True, blank = True, upload_to = 'images/%y/definicija3/nedjelja' )
    vjezbe = models.CharField(max_length=200)
    serije = models.IntegerField()
    ponavljanja = models.CharField(max_length=300)

    def __str__(self):
   
        return self.vjezbe
        return self.serije 
        return self.ponavljanja


    class Meta:
        verbose_name_plural = "Misicna_definicija3_nedjelja"



#################################################################################



#plaćanje 


class Placanje(models.Model):
    naslov = models.CharField(max_length=200)
    cijena = models.IntegerField()
    kategorije = models.TextField()

    


    def __str__(self):
        return self.naslov
        return self.cijena
        return self.kategorije
      

    class Meta:
        verbose_name_plural = "Placanje"



class Order(models.Model):
	product = models.ForeignKey(Placanje, max_length=200, null=True, blank=True, on_delete = models.SET_NULL)
	created =  models.DateTimeField(auto_now_add=True) 

	def __str__(self):
		return self.product.name
    
    


 

