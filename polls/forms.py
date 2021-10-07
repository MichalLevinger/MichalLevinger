from django import forms

from .models import Person, Address

class RegisterPersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'address']
