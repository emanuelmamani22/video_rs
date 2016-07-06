from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegistroUserForm, login_user, subirvideo
from django.contrib.auth import authenticate, login, logout
from .models import UploadVideo, Tagvideo, Perfil, Canal, Subcriptores
from .funciones import calcular_codigo
# Create your views here.

def index(request):
  bienvenido = 'Bienvenido'
  return render(request, 'index.html', {'bienvenido':bienvenido})

def registro_user(request):
  if request.method == 'POST':
    form = RegistroUserForm(request.POST)
    if form.is_valid():
      namefirst = request.POST['namefirst']
      namelast = request.POST['namelast']
      username = request.POST['username']
      email = request.POST['email']
      password = request.POST['password']

      insert = User.objects.create_user(password=password, username=username, email=email, first_name=namefirst, last_name=namelast)
      insert.save()
     
      return redirect('index')
    else :
      return render(request, 'registro.html', {'form': form})
  else :
    form = RegistroUserForm()
    return render(request, 'registro.html', {'form':form})

def login_views(request):
  message = None
  if request.method == 'POST':
    form = login_user(request.POST)
    if form.is_valid():
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(username=username, password=password)
      if user is not None:
        if user.is_active:
          login(request, user)
          return HttpResponseRedirect('/')
        else :
          message = 'Tu usuario esta inactivo'
      else :
          message = "Nombre de usuario y/o password incorrecto"
    else :
      return render(request, 'login.html', {'message':message,'form':form})
  else :
    form = login_user()
  return render(request, 'login.html', {'message':message, 'form':form})

def logout_views(request): 
    logout(request)    
    return redirect('index')

def up_video(request):
    if request.user.is_authenticated():
      if request.method == 'POST':
        form = subirvideo(request.POST, request.FILES)
        if form.is_valid():
          namevideo = request.POST['nombre_video']
          video_archivo = request.FILES['archivo_video']
          tag_video = request.POST['video_tag']
          q = Tagvideo.objects.get(id_tag=int(tag_video))
          canal = Canal.objects.get(id_u=request.user)
          cod = calcular_codigo()
          video = UploadVideo(cod_video=cod, nombre_video=namevideo, video_file=video_archivo, id_c=canal, id_tag=q)
          video.save()

          return HttpResponseRedirect('/')
        else :
          return render(request, 'up_video.html', {'form':form})
      else :
        form = subirvideo()
    else :
      return HttpResponseRedirect('/login')
    return render(request, 'up_video.html', {'form':form})

def watchvideo(request):
      vervideo = 'vervideo.html'
      x = request.GET.get('v','')
      q = UploadVideo.objects.get(cod_video=x)
      if request.method == 'POST':
        if request.user.is_authenticated():
          u = request.user
          y = User.objects.get(username=u)
          r = Canal.objects.get(id_canal=q.id_c.id_canal)
          try :
             z = Subcriptores.objects.get(id_u=y.id, id_c=r)
             z.delete()
             return render(request, vervideo, {'q':q})
          except Subcriptores.DoesNotExist:
             r = Canal.objects.get(id_canal=q.id_c.id_canal)
             s = Subcriptores(id_c=r, id_u=u)
             s.save()

             return render(request, vervideo, {'q':q})
        else :
          return HttpResponseRedirect('/login')
      else :
        return render(request, vervideo, {'q':q})









