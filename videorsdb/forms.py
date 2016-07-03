from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
import magic
from .funciones import choice_tag

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
          raise forms.ValidationError('Nombre de usuario ya registrado.')
       return user_name
       
     def clean_email(self):
       user_email = self.cleaned_data['email']
       if User.objects.filter(email=user_email):
          raise forms.ValidationError('Correo electronico ya registrado.')
       return user_email

     def clean_passworddos(self):
       user_pass = self.cleaned_data['password']
       user_passdos = self.cleaned_data['passworddos']
       if user_pass != user_passdos:
          raise forms.ValidationError('Las contrasenias no son iguales.')
       return user_passdos

class login_user(forms.Form):
     username = forms.CharField(min_length=5)
     password = forms.CharField(min_length=5, widget=forms.PasswordInput())

class subirvideo(forms.Form):
     nombre_video = forms.CharField(min_length=5)
     archivo_video = forms.FileField()
     video_tag = forms.ChoiceField(widget=forms.Select(),choices=choice_tag())

     def clean_subirvideo(self):
       file_f = self.cleaned_data['archivo_video']
       mime = magic.from_buffer(file_f.read(), mime=True)
       if mime != 'video/mp4':
          raise forms.ValidationError('Sube un archivo de MP4.')
       return file_f
