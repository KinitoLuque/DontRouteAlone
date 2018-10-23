"""DontRouteAlone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from DRAapp import views
from DRAapp.views import ListaRuta, CreaUsuario, CreaRuta, ActualizaUsuario, ActualizaRuta, BorraUsuario, BorraRuta

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.base, name='base'),
    url(r'^rutas/$', ListaRuta.as_view()),
    url(r'usuario/add/$', CreaUsuario.as_view(), name='crea-usuario'),
    url(r'usuario/(?P<pk>[0-9]+)/$', ActualizaUsuario.as_view(), name='actualiza-usuario'),
    url(r'usuario/(?P<pk>[0-9]+)/delete/$', BorraUsuario.as_view(), name='borra-usuario'),
    url(r'ruta/add/$', CreaRuta.as_view(), name='crea-ruta'),
    url(r'ruta/(?P<pk>[0-9]+)/$', ActualizaRuta.as_view(), name='actualiza-ruta'),
    url(r'ruta/(?P<pk>[0-9]+)/delete/$', BorraRuta.as_view(), name='borra-ruta')
]
