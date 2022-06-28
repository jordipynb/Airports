from django.urls import path, re_path
from .views.home import home
from .views.listar import listar
from .views.registrar import registrar
from .views.edicion import edicion
from .views.editar import editar
from .views.eliminar import eliminar
from authn.views import register
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', home),
    path('listar/', listar),
    path('registrar/', registrar),
    path('listar/edicion/<codigo>/<tabla>/<campos>', edicion),
    path('editar/', editar),
    path('listar/eliminar/<codigo>/<tabla>', eliminar),
    path('register/', register, name='register'),
    ]
