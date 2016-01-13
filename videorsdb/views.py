from django.shortcuts import render

# Create your views here.

def index(request):
  bienvenido = 'Bienvenido'
  return render(request, 'index.html', {'bienvenido':bienvenido})
