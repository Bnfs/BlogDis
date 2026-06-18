from django.core import validators
from django import forms
from .models import Contact,Comment

class ContactRegistration(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['nom','email','sujet','message']
        widgets={

        }
class CommentsRegistration(forms.ModelForm):
    # Champ piege anti-spam : invisible pour un humain, mais souvent rempli
    # par les robots. S'il est rempli, le commentaire est rejete.
    website=forms.CharField(required=False,widget=forms.HiddenInput,label='')

    class Meta:
        model=Comment
        fields=['nom','email','commentaire']
        widgets={
            'nom':forms.TextInput(attrs={'class':'form-control','placeholder':'Votre nom'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Votre email (non publié)'}),
            'commentaire':forms.Textarea(attrs={'class':'form-control','rows':'5','placeholder':'Votre commentaire'}),
        }
    