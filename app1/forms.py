from django import forms
from .models import Person
from django.forms import widgets


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name','plate_num','status',]
        widgets={
           'name':forms.TextInput(attrs={'class':'form-control'}),
           'plate_num': forms.TextInput(attrs={'class': 'form-control'}),
           'status': forms.TextInput(attrs={'class': 'form-control'}),
       }




