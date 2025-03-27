from django import forms
from .models import Employee

class EmpForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'pwd']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'pwd': forms.PasswordInput(render_value=True,attrs={'class': 'form-control'}),
        }
