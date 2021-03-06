"""video_rs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from videorsdb import views
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', 'videorsdb.views.registro_user', name='registrarse'),
    url(r'^login/$', 'videorsdb.views.login_views', name='login'),
    url(r'^logout/$', 'videorsdb.views.logout_views', name='logout'),
    url(r'^uploadvideo/$', 'videorsdb.views.up_video', name='subirvideo'),
    url(r'^watch$', 'videorsdb.views.watchvideo', name='vervideo'),
    url(r'^crearcanal/$', 'videorsdb.views.cretechannel', name='crearcanal'),
    url(r'^canal/(?P<channel>[^/]{20})/$', 'videorsdb.views.viewchannel', name='channel'),
    url(r'^eliminar/(?P<delete>[^/]{11})/$', 'videorsdb.views.deletevideo', name='delete'),
    url(r'^ajaxsubs/$', 'videorsdb.views.subs_ajax', name='subsajax'),
    url(r'^ajaxcomentar/$', 'videorsdb.views.comentar_ajax', name='comentarajax'),
    url(r'^ajaxmegusta/$', 'videorsdb.views.megusta_ajax', name='megustaajax'),
    url(r'^ajaxnomegusta/$', 'videorsdb.views.nomegusta_ajax', name='nomegustaajax'),
    url(r'^result$', 'videorsdb.views.resultado', name='resultado'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
   ]
