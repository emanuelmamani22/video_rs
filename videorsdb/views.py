from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegistroUserForm, login_user, subirvideo
from django.contrib.auth import authenticate, login, logout
from .models import DownloadVideo
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
          usuario = request.user
          cod = calcular_codigo()
          video = DownloadVideo(cod_video=cod, nombre_video=namevideo, video_file=video_archivo, id_u=usuario)
          video.save()

          return HttpResponseRedirect('/')
        else :
          return render(request, 'up_video.html', {'form':form})
      else :
        form = subirvideo()
    else :
      return HttpResponseRedirect('/login')
    return render(request, 'up_video.html', {'form':form})
