from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegistroUserForm
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
      email = request.Post['email']
      password = request.Post['password']
     
      insert = User.objects.create_user(password=password, username=username, email=email, first_name=namefirst, last_name=namelast)
      insert.save()
     
      return redirect('index')
    else :
      return render(request, 'registro.html', {'form': form})
  else :
    form = RegistroUserForm()
    return render(request, 'registro.html', {'form':form})
