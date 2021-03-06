from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
import magic
from .funciones import choice_tag, getLength
import re
from PIL import Image

class RegistroUserForm(forms.Form):
     namefirst = forms.CharField(min_length=5, widget=forms.TextInput(attrs={'class':'validate', 'id': 'first_name'}), error_messages={'required': 'Nombre obligatorio'})
     namelast = forms.CharField(min_length=5, widget=forms.TextInput(attrs={'class':'validate', 'id': 'last_name'}), error_messages={'required': 'Apellido obligatorio'})
     username = forms.CharField(min_length=5, widget=forms.TextInput(attrs={'class':'validate', 'id': 'username'}), error_messages={'required': 'Nombre de usuario obligatorio'})
     email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'validate', 'id': 'email'}), error_messages={'required': 'Email obligatorio'})
     password = forms.CharField(min_length=5, widget=forms.PasswordInput(attrs={'class':'validate', 'id': 'password'}), error_messages={'required': 'Password obligatorio'})
     passworddos = forms.CharField(widget=forms.PasswordInput(attrs={'class':'validate', 'id': 'passworddos'}), error_messages={'required': 'Debe repetir el password'})

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
     username = forms.CharField(min_length=5, widget=forms.TextInput(attrs={'class':'validate', 'id': 'username'}), error_messages={'required': 'Indica tu nombre de usuario'})
     password = forms.CharField(min_length=5, widget=forms.PasswordInput(attrs={'class':'validate', 'id': 'first_name'}), error_messages={'required': 'Indica el password'})

class crear_canal(forms.Form):
     nombre_canal = forms.CharField(min_length=5,widget=forms.TextInput(attrs={'class':'validate', 'id': 'crear_canal'}), error_messages={'required': 'Escribe el nombre del canal'})
     portada = forms.FileField(error_messages={'required': 'Es necesario que agregues una portada'})
     descripcion = forms.CharField(min_length=5, widget=forms.TextInput(attrs={'class':'validate', 'id': 'crear_canal'}), error_messages={'required': 'Es necesario que des una descripcion de tu canal'})

     def clean_portada(self):
       portada_f = self.cleaned_data['portada']
       mime = magic.from_buffer(portada_f.read(), mime=True)
       if mime != 'image/jpeg':
         raise forms.ValidationError('Sube un portada jpeg.')

       #file_p = portada_f.temporary_file_path()
       im=Image.open(portada_f)
       size_img = im.size

       if size_img[0] != 2120:
         raise forms.ValidationError('La portada del canal debe ser de 2120px de ancho.')

       if size_img[1] != 351:
         raise forms.ValidationError('La portada del canal debe ser de 351px de alto.')

       return portada_f


class subirvideo(forms.Form):
    nombre_video = forms.CharField(min_length=5, error_messages={'required': 'Agrega un nombre al video'})
    archivo_video = forms.FileField(error_messages={'required': 'Selecciona un video'})
    video_tag = forms.ChoiceField(widget=forms.Select(),choices=choice_tag())
    miniatura_video = forms.FileField(error_messages={'required': 'Es necesario que agregues una miniatura'})

    def clean_archivo_video(self):
      file_f = self.cleaned_data['archivo_video']
      mime = magic.from_buffer(file_f.read(), mime=True)
      if mime != 'video/mp4':
        raise forms.ValidationError('Sube un archivo de MP4.')

      file_v = file_f.temporary_file_path()
      a = getLength(file_v)
      try:
          url = re.search('  Duration: ([^/]{8,11}),', a[0]).group(1)
          print url
          if url > '00:15:00' :
              raise forms.ValidationError('El video no puede durar mas de 15 minutos.')
      except AttributeError:
          raise forms.ValidationError('Error inesperado intentelo de nuevo.')
      return file_f

    def clean_miniatura_video(self):
      miniatura_f = self.cleaned_data['miniatura_video']
      mime = magic.from_buffer(miniatura_f.read(), mime=True)
      if mime != 'image/jpeg':
        raise forms.ValidationError('Sube un miniatura jpeg.')
      
      file_i = miniatura_f.temporary_file_path()
      im=Image.open(file_i)
      size_img = im.size

      if size_img[0] != 260:
        raise forms.ValidationError('La miniatura del video debe ser de 260px de ancho.')

      if size_img[1] != 146:
        raise forms.ValidationError('La miniatura del video debe ser de 146px de alto.')

class comentario_form(forms.Form):
  comentario = forms.CharField(widget=forms.Textarea(attrs={'class':'materialize-textarea', 'placeholder':'Escribe un comentario'}))