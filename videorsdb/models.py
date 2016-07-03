from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tagvideo(models.Model):
    id_tag = models.AutoField(primary_key=True)
    nombre_tag = models.CharField(max_length=70)
    
    def __unicode__(self):
       return self.nombre_tag

class UploadVideo(models.Model):
    id_video = models.AutoField(primary_key=True)
    cod_video = models.CharField(max_length=11)
    nombre_video = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='video/', max_length=200)
    id_u = models.ForeignKey(User, null=True)
    id_tag = models.ForeignKey(Tagvideo)

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to='avatar/', max_length=200)
    subscriptores = models.ManyToManyField('self')


