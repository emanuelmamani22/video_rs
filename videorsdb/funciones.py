import random
from .models import UploadVideo, Tagvideo

def calcular_codigo():
    a=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','_','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','-','O','P','Q','R','S','T','U','V','W','X','Y','Z',]
    b=''
    c=0
    while c < 11 :
      d=random.randrange(0,64)
      b=b+a[d]
      c=c+1
    if UploadVideo.objects.filter(cod_video=b):
       calcular_codigo()
    
    return b


def choice_tag():
  from django.db import connection
  cursor = connection.cursor()
  cursor.execute("""SELECT videorsdb_tagvideo.id_tag, videorsdb_tagvideo.nombre_tag FROM public.videorsdb_tagvideo""")
  row = cursor.fetchall()
  #choice_field=((str(row[0][0]), row[0][1],), (str(row[1][0], row[1][1],),(str(row[2][0]), row[2][1],),(str(row[3][0]), row[3][1],))
  CHOICES = (('1', row[0][1],), ('2', row[1][1],),('2', row[2][1],),('2', row[3][1],),('2', row[4][1],),('2', row[5][1],),('2', row[6][1],),('2', row[7][1],),('2', row[8][1],),('2', row[9][1],))
  return CHOICES
