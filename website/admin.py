from django.contrib import admin
from .models import Cetvrti_program_cetvrtak, Cetvrti_program_petak, Cetvrti_program_ponedjeljak, Cetvrti_program_srijeda, Cetvrti_program_subota, Cetvrti_program_utorak, Drugi_program_cetvrtak, Drugi_program_petak, Drugi_program_ponedjeljak, Drugi_program_srijeda, Drugi_program_subota, Drugi_program_utorak, Misicna_definicija2_petak, Misicna_definicija2_ponedjeljak, Misicna_definicija3_nedjelja, Misicna_definicija3_petak, Misicna_definicija3_ponedjeljak, Misicna_definicija_petak, Misicna_definicija_ponedjeljak, Misicna_definicija_srijeda, Misicna_definicija_srijeda2, Misicna_definicija_srijeda3, Placanje, Program_mass2_cetvrtak, Program_mass2_petak, Program_mass2_ponedjeljak, Program_mass2_utorak, Program_mass_cetvrtak, Program_mass_petak, Program_mass_ponedjeljak, Program_mass_utorak, Program_snaga_petak, Program_snaga_ponedjeljak, Program_snaga_srijeda, Program_yoga, Prvi_program_ponedjeljak, Prvi_program_cetvrtak, Prvi_program_petak, Prvi_program_ponedjeljak, Prvi_program_srijeda, Prvi_program_subota, Prvi_program_utorak, Treci_program_cetvrtak, Treci_program_petak, Treci_program_ponedjeljak, Treci_program_srijeda, Treci_program_subota, Treci_program_utorak, Program_yoga



#prvi program core

admin.site.register(Prvi_program_ponedjeljak)
admin.site.register(Prvi_program_utorak)
admin.site.register(Prvi_program_srijeda)
admin.site.register(Prvi_program_cetvrtak)
admin.site.register(Prvi_program_petak)
admin.site.register(Prvi_program_subota)


#drugi program core



admin.site.register(Drugi_program_ponedjeljak)
admin.site.register(Drugi_program_utorak)
admin.site.register(Drugi_program_srijeda)
admin.site.register(Drugi_program_cetvrtak)
admin.site.register(Drugi_program_petak)
admin.site.register(Drugi_program_subota)




#treci program core



admin.site.register(Treci_program_ponedjeljak)
admin.site.register(Treci_program_utorak)
admin.site.register(Treci_program_srijeda)
admin.site.register(Treci_program_cetvrtak)
admin.site.register(Treci_program_petak)
admin.site.register(Treci_program_subota)


#cetvrti program core



admin.site.register(Cetvrti_program_ponedjeljak)
admin.site.register(Cetvrti_program_utorak)
admin.site.register(Cetvrti_program_srijeda)
admin.site.register(Cetvrti_program_cetvrtak)
admin.site.register(Cetvrti_program_petak)
admin.site.register(Cetvrti_program_subota)


#PROGRAM MASS GAIN

admin.site.register(Program_mass_ponedjeljak)
admin.site.register(Program_mass_utorak)
admin.site.register(Program_mass_cetvrtak)
admin.site.register(Program_mass_petak)



#PROGRAM MASS GAIN 2

admin.site.register(Program_mass2_ponedjeljak)
admin.site.register(Program_mass2_utorak)
admin.site.register(Program_mass2_cetvrtak)
admin.site.register(Program_mass2_petak)





#PROGRAM SNAGA

admin.site.register(Program_snaga_ponedjeljak)
admin.site.register(Program_snaga_srijeda)
admin.site.register(Program_snaga_petak)


#PROGRAM DEFINICIJA###################################################

admin.site.register(Misicna_definicija_ponedjeljak)
admin.site.register(Misicna_definicija_srijeda)
admin.site.register(Misicna_definicija_petak)

#################################################################



#PROGRAM DEFINICIJA 2###################################################

admin.site.register(Misicna_definicija2_ponedjeljak)
admin.site.register(Misicna_definicija_srijeda2)
admin.site.register(Misicna_definicija2_petak)

#################################################################


#PROGRAM DEFINICIJA 3###################################################

admin.site.register(Misicna_definicija3_ponedjeljak)
admin.site.register(Misicna_definicija_srijeda3)
admin.site.register(Misicna_definicija3_petak)
admin.site.register(Misicna_definicija3_nedjelja)

#################################################################

#yoga


admin.site.register(Program_yoga)

#placanje

admin.site.register(Placanje)
