from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tagvideo(models.Model):
    id_tag = models.AutoField(primary_key=True)
    nombre_tag = models.CharField(max_length=70)
    
    def __unicode__(self):
       return self.nombre_tag

class Canal(models.Model):
    id_canal = models.AutoField(primary_key=True)
    codigo_canal = models.CharField(blank=True, max_length=20)
    nombre = models.CharField(max_length=70)
    id_u = models.ForeignKey(User)

    def __unicode__(self):
       return self.nombre

class UploadVideo(models.Model):
    id_video = models.AutoField(primary_key=True)
    cod_video = models.CharField(max_length=11)
    nombre_video = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='video/', max_length=200)
    id_c = models.ForeignKey(Canal)
    id_tag = models.ForeignKey(Tagvideo)

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to='avatar/', max_length=200)
    
    def __unicode__(self):
       return self.usuario

class Subcriptores(models.Model):
    id_subs = models.AutoField(primary_key=True)
    id_c = models.ForeignKey(Canal)
    id_u = models.ForeignKey(User)
