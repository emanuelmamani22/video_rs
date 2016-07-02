from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

class RegistroUserForm(forms.Form):
     namefirst = forms.CharField(min_length=5)
     namelast = forms.CharField(min_length=5)
     username = forms.CharField(min_length=5)
     email = forms.EmailField()
     password = forms.CharField(min_length=5, widget=forms.PasswordInput())
     passworddos = forms.CharField(widget=forms.PasswordInput())

     def clean_username(self):
       user_name = self.cleaned_data['username']
       if User.objects.filter(username=user_name):
          raise form.ValidationError('Nombre de usuario ya registrado.')
       return user_name
       
     def clean_email(self):
       user_email = self.cleaned_data['email']
       if User.objects.filter(email=user_email):
          raise form.ValidationError('Correo electronico ya registrado.')
       return user_email

     def clean_passworddos(self):
       user_pass = self.cleaned_data['password']
       user_passdos = self.cleaned_data['passworddos']
       if user_pass != user_passdos:
          raise form.ValidationError('Las contrasenias no son iguales.')
       return user_passdos
