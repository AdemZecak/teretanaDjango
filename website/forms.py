from django import forms 
from .models import Prvi_program_ponedjeljak



class ListForm(forms.ModelForm):
    class Meta:
        model = Prvi_program_ponedjeljak
        fields = ["gif","vjezbe","serije","ponavljanja","completed"]