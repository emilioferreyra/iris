# -*- coding: utf-8 -*-
from django import forms
from .models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('names', 'father_last_name', 'mother_last_name')
        widgets = {
            'names': forms.TextInput(attrs={'placeholder': 'Nombres'}),
            'father_last_name':
                forms.TextInput(attrs={'placeholder': 'Primer apellido'}),
            'mother_last_name':
                forms.TextInput(attrs={'placeholder': 'Segundo apellido'}),
            'email': forms.EmailInput(attrs={'placeholder': 'e-mail'}),
            'document_id':
                forms.TextInput(attrs={'placeholder': 'Cédula o pasaporte'}),
        }
