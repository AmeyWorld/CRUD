from django.core import validators
from django import forms
from .models import student_info

class student_reg(forms.ModelForm):
    class Meta:
        model = student_info
        # fields = '__all__'
        fields = ['name', 'email', 'password']
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True, attrs={'class':'form-control'})

        }
