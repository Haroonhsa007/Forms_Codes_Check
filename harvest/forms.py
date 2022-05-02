from django import forms
from django.forms import ModelForm

from .models import Person


class PersonForm(ModelForm):

    class Meta:
        model = Person
        fields = ('id', 'sex', 'age')
        labels = {
            'id': '',
            'sex': '',
            'age': ''
        }

        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ID'}),
            'sex': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sex'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
        }
