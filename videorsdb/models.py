from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class DownloadVideo(models.Model):
    id_video = models.AutoField(primary_key=True)
    cod_video = models.CharField(max_length=11)
    nombre_video = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='video/', max_length=200)
    id_u = models.ForeignKey(User)
