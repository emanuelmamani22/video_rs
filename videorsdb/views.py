from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegistroUserForm, login_user, subirvideo, crear_canal, comentario_form
from django.contrib.auth import authenticate, login, logout
from .models import UploadVideo, Tagvideo, Perfil, Canal, Subcriptores, Comentario, Likeanddislike
from .funciones import calcular_codigo, likesave, likeanddislikedelete, dislikesave
from django.http import Http404
from django.contrib.auth.decorators import login_required
import random

#Procesadres de Contexto
def subcripciones_user(request):
	u = request.user
	sub_ctx = Subcriptores.objects.filter(id_u=u.id)
	return {'sub_ctx':sub_ctx,}

def canal_user(request):
	user_ctx = request.user
	try :
		user_canal = Canal.objects.get(id_u=user_ctx.id)
		return {'user_canal': user_canal, 'user_ctx':user_ctx}
	except Canal.DoesNotExist:
		user_canal = None
		return {'user_canal': user_canal, 'user_ctx':user_ctx}

def sugerencias(request):
	r=random.randrange(1,10)
	s1 = UploadVideo.objects.filter(id_tag=r).order_by('?')[:4]
	return {'s1':s1,}
# Create your views here.

def index(request):
	r=random.randrange(1,10)
	q = UploadVideo.objects.filter(id_tag=r).order_by('?')[:4]
	name_q = q[0].id_tag.nombre_tag 
	if request.user.is_authenticated():
		user = request.user
		ureco = Likeanddislike.objects.filter(id_u=user.id, megusta=True).order_by('?')[:4]
		return render(request, 'index.html', {'q':q, 'hola':'hola','name_q':name_q, 'ureco':ureco}, context_instance=RequestContext(request, processors=[canal_user, subcripciones_user]))
	return render(request, 'index.html', {'q':q,'name_q':name_q, 'hola':'hola'},)

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

def cretechanell(request):
    if request.user.is_authenticated():
      if request.method == 'POST':
         form = crear_canal(request.POST)
         if form.is_valid():
           nombre_canal = request.POST['nombre_canal']
           cod = calcular_codigo(20)
           usuario = request.user
           canal = Canal(codigo_canal=cod, nombre=nombre_canal, id_u=usuario)
           canal.save()
           
           return HttpResponseRedirect('/')
         else :
           return render(request, 'crearcanal.html', {'form':form})
      else:
         form = crear_canal()
         return render(request, 'crearcanal.html', {'form':form})
    else :
      return HttpResponseRedirect('/login')
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
          cod = calcular_codigo(11)
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
	u = request.user
	vervideo = 'vervideo.html'
	x = request.GET.get('v','')
	q = UploadVideo.objects.get(cod_video=x)
	c = Comentario.objects.filter(id_v=q.id_video)
	form = comentario_form()
	contarlike = Likeanddislike.objects.filter(id_v=q, megusta=True).count()
	contardislike = Likeanddislike.objects.filter(id_v=q, nomegusta=True).count()
	return render(request, vervideo, {'q':q, 'form':form,'c':c, 'contarlike':contarlike, 'contardislike':contardislike}, context_instance=RequestContext(request, processors=[sugerencias,]))


def viewchannel(request, channel):
	q = Canal.objects.get(codigo_canal=channel)
	z = UploadVideo.objects.filter(id_c=q.id_canal)
	if request.user == q.id_u :
		return render(request, 'channeladmin.html', {'q':q, 'z':z}, context_instance=RequestContext(request, processors=[canal_user, subcripciones_user]))
	else :
		if request.method == 'POST':
			if request.user.is_authenticated():
				u = request.user
				y = User.objects.get(username=u)
				try :
					s = Subcriptores.objects.get(id_u=y.id, id_c=q.id_canal)
					s.delete()
					return render(request, 'channel.html', {'q':q, 'z':z})
				except Subcriptores.DoesNotExist:
					r = Canal.objects.get(id_canal=q.id_canal)
					s = Subcriptores(id_c=r, id_u=u)
					s.save()

					return render(request, 'channel.html', {'q':q, 'z':z})
			else :
				return HttpResponseRedirect('/login')
		else :
			return render(request, 'channel.html', {'q':q, 'z':z})

def deletevideo(request, delete):
	if request.user.is_authenticated():
		u = request.user
		m = Canal.objects.get(id_u = u)
		q = UploadVideo.objects.get(cod_video = delete)
		if m.id_canal == q.id_c :
			q.delete()
			return HttpResponseRedirect('/')
		else :
			return HttpResponseRedirect('/login')
	else :
		return HttpResponseRedirect('/login')

def subs_ajax(request):
	x = request.POST['video_cod']
	q = UploadVideo.objects.get(cod_video=x)
	r = Canal.objects.get(id_canal=q.id_c.id_canal)
	if request.method == 'POST':
			if request.user.is_authenticated():
				u = request.user
				y = User.objects.get(username=u)
				try :
					subs = Subcriptores.objects.get(id_u=y.id, id_c=r)
					subs.delete()
					return HttpResponse()
				except Subcriptores.DoesNotExist:
					subs = Subcriptores(id_c=r, id_u=u)
					subs.save()

					return HttpResponse()
			else :
				return HttpResponse('/login')
	else :
		return HttpResponseRedirect('/')

def comentar_ajax(request):
	x = request.POST['video_cod']
	c = request.POST['comentario']
	q = UploadVideo.objects.get(cod_video=x)
	if request.method == 'POST':
			if request.user.is_authenticated():
				u = request.user
				y = User.objects.get(username=u)
				coments = Comentario(comentario_text = c, id_v=q, id_user=u)
				coments.save()
				return HttpResponse()
			else :
				return HttpResponse('/login')
	else :
		return HttpResponseRedirect('/')

def megusta_ajax(request):
	x = request.POST['video_cod']
	q = UploadVideo.objects.get(cod_video=x)
	if request.method == 'POST':
			if request.user.is_authenticated():
				try :
					u = request.user
					y = User.objects.get(username=u)
					if Likeanddislike.objects.get(id_v=q, id_u=y, megusta=True, nomegusta=False):
						likeanddislikedelete(q, y)

						return HttpResponse()
	 			except Likeanddislike.DoesNotExist:
	 				try :
	 					likeanddislikedelete(q, y)
	 					likesave(q, y)
					except Likeanddislike.DoesNotExist:
						likesave(q, y)

					return HttpResponse()
			else :
				return HttpResponse('/login')
	else :
		return HttpResponseRedirect('/')

def nomegusta_ajax(request):
	x = request.POST['video_cod']
	q = UploadVideo.objects.get(cod_video=x)
	if request.method == 'POST':
			if request.user.is_authenticated():
				try :
					u = request.user
					y = User.objects.get(username=u)
					if Likeanddislike.objects.get(id_v=q, id_u=y, megusta=False, nomegusta=True):
						likeanddislikedelete(q, y)

						return HttpResponse()
	 			except Likeanddislike.DoesNotExist:
	 				try :
	 					likeanddislikedelete(q, y)
	 					dislikesave(q, y)
					except Likeanddislike.DoesNotExist:
						dislikesave(q, y)

					return HttpResponse()
			else :
				return HttpResponse('/login')
	else :
		return HttpResponseRedirect('/')

def resultado(request):
	x = request.GET.get('search_query','')
	q = UploadVideo.objects.filter(nombre_video__contains=x)
	return render(request, 'resultado.html', {'q':q})