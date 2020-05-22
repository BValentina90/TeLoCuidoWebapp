from .models import Registro, Cuidacoches, Conductor
from django import forms

class ValidacionCuidacoches(forms.ModelForm):
    class Meta:
        model = Cuidacoches
        fields = [
            'ci',
            'num_registro',
            ]


        labels = {
            'ci': 'Cédula de Identidad',
            'num_registro': 'Número de Registro',}

        widgets = {
            'ci': forms.TextInput(attrs={'class':'form-control'}),
            'num_registro': forms.TextInput(attrs={'class':'form-control'}),
            }


class RegistroCuidacochesApp(forms.ModelForm):
    class Meta:
        model = Cuidacoches
        fields = [
            'cant_lugares',
            'telefono',
            'mail',
            'cuenta_bancaria',
            'banco',
            'password'
        ]

        labels = {
        'cant_lugares': 'Ingrese cantidad de lugares',
        'telefono': 'Teléfono',
        'mail': 'Mail',
        'cuenta_bancaria': 'Num de cuenta bancaria',
        'banco': 'Nombre del Banco',
        'password': 'Contraseña',
        }

        widgets = {
        'cant_lugares': forms.TextInput(attrs={'class':'form-control'}),
        'telefono': forms.TextInput(attrs={'class':'form-control'}),
        'mail': forms.TextInput(attrs={'class':'form-control'}),
        'cuenta_bancaria': forms.TextInput(attrs={'class':'form-control'}),
        'banco': forms.TextInput(attrs={'class':'form-control'}),
        'password': forms.PasswordInput(attrs={'class':'form-control'}),
        }


class ConductorForm(forms.ModelForm):
    class Meta:
        model = Conductor
        fields = [
            'nombre',
            'apellido',
            'ci',
            'telefono',
            'mail',
            'cuenta_bancaria',
            'banco',
            'password',
            ]

        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'ci': 'Cédula de identidad',
            'telefono': 'Teléfono',
            'mail': 'Mail',
            'cuenta_bancaria': 'Num de cuenta bancaria',
            'banco': 'Nombre del banco',
            'password': 'Contraseña',
            }

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'ci': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'mail': forms.TextInput(attrs={'class':'form-control'}),
            'cuenta_bancaria': forms.TextInput(attrs={'class':'form-control'}),
            'banco': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
            }


class LoginForm(forms.Form):

    ci = forms.CharField(label='C.I.', max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='CONTRASEÑA', max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control'}))


class OcuparForm(forms.Form):
    ocupar_espacio = forms.CharField(label='',max_length=1, widget=forms.TextInput(attrs={'style':'display: none', 'value': '1'}))

class LiberarForm(forms.Form):
    liberar_espacio = forms.CharField(label='',max_length=1, widget=forms.TextInput(attrs={'style':'display: none', 'value': '1'}))

    