from django.shortcuts import redirect, render
from django.contrib import messages
from accounts.models import Usuario

from model.models.Aeropuerto import Aeropuerto
from model.models.Cliente import Cliente
from model.models.Nave import Nave
from model.models.Vuelo import Vuelo
from model.models.Arribo import Arribo
from model.models.Instalacion import Instalacion
from model.models.Servicio import Servicio
from model.models.Valoracion import Valoracion
from model.models.Reparacion import Reparacion
from model.models.ReparaNave import ReparaNave
from model.models.ReparacionesDependientes import ReparacionesDependientes

def listar(request):
    dict=para_listar(request)
    return render(request, "listados.html", dict)

def para_listar(request):
    data = str(request.GET['data'])
    listado=[]
    name = ""
    if data == "Aeropuerto":
        listado = Aeropuerto.objects.all()
        name = "Aeropuertos" 
    elif data == "Cliente":
        listado = Cliente.objects.all()
        name = "Clientes"
    elif data == "Nave":
        listado = Nave.objects.all()
        name = "Naves"
    elif data == "Vuelo":
        listado = Vuelo.objects.all()
        name = "Vuelos"
    elif data == "Arribo":
        listado = Arribo.objects.all()
        name = "Arribos"
    elif data == "Instalacion":
        listado = Instalacion.objects.all()
        name = "Instalaciones"
    elif data == "Servicio":
        listado = Servicio.objects.all()
        name = "Servicios"
    elif data == "Valoracion":
        listado = Valoracion.objects.all()
        name = "Valoraciones"
    elif data == "Reparacion":
        listado = Reparacion.objects.all()
        name = "Reparaciones"
    elif data == "ReparaNave":
        listado = ReparaNave.objects.all()
        name = "Reparaciones de Naves"
    elif data == "ReparacionesDependientes":
        listado = ReparacionesDependientes.objects.all()
        name = "Reparaciones Dependientes"
    elif data == "Admin_de_Instalacion":
        listado = Usuario.objects.all()
        name = "Administradores de Instalaciones"
    #messages.success(request, 'Listados!')
    campos=[]
    for a in listado:
         campos=a.campos()
         break
    print(len(campos))
    
    return {"campos": campos,"aeropuertos": listado,"tabla":data, "name": name}

