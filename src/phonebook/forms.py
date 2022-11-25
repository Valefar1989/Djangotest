from django import forms

from . import models

class CreatePersoneFrom(forms.ModelForm):
    phones = forms.CharField(widget=forms.Textarea())
    class Meta:
        model = models.Persona
        fields = (
            'name',
            'phones'
        )
    
