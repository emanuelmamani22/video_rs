from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Canal(models.Model):
    id_canal = models.AutoField(primary_key=True)
    nombre_canal = models.CharField(max_length=20)
    duenio_de_canal = models.ForeignKey(User)

class Subscriptores(models.Model):
    id_canal = models.ForeignKey(Canal)
    subscriptor = models.ForeignKey(User)

class DownloadVideo(models.Model):
    id_video = models.AutoField(primary_key=True)
    cod_video = models.CharField(max_length=11)
    nombre_video = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='video/', max_length=200)
    id_c = models.ForeignKey(Canal, null=True)

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to='avatar/', max_length=200)
