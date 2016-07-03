import random
from .models import UploadVideo


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
