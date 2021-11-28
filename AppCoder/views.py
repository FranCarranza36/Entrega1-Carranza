from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from AppCoder.forms import FutbolistasFormulario, BasquetbolistasFormulario, TenistasFormulario
from .models import Futbolista, Basquetbolista, Tenista

# Create your views here.

def index(request):
    return render(request, 'AppCoder/index.html', {})

def lista_futbolistas(request):
    futbolistas = None
    error_nombre = None
    error_apellido = None
    error_edad = None
    if request.method =='GET':
        nombre = request.GET.get('nombre', '')
        apellido = request.GET.get('apellido','')
        edad = request.GET.get('edad',None)
        if nombre == '' and apellido == '' and edad == '' : #Se considera que si no introdujo ningún campo, está queriendo ver todos.
            futbolistas = Futbolista.objects.all()
        elif nombre: 
            if nombre.replace(' ','').isalpha():
                futbolistas = Futbolista.objects.filter(nombre = nombre)
            else:
                error_nombre = 'Debe ingresar un nombre válido'
        
        elif apellido:
            if apellido.replace(' ','').isalpha():
                futbolistas = Futbolista.objects.filter(apellido = apellido)
            else:
                error_apellido = 'Debe ingresar un apellido válido'
                
        elif edad:
            try: 
                edad = int(edad)
                futbolistas = Futbolista.objects.filter(edad = edad)
            except:
                error_edad = 'Debe ingresar una edad válida'   
                         
    return render(request, 'AppCoder/lista_futbolistas.html', {'futbolistas': futbolistas, 'error_nombre': error_nombre, 'error_apellido': error_apellido, 'error_edad': error_edad})        

def crear_futbolista(request):
    if request.method == 'POST':
        formulario = FutbolistasFormulario(request.POST)
        
        if formulario. is_valid():
            datos_futbolista = formulario.cleaned_data
            futbolista = Futbolista(nombre = datos_futbolista['nombre'], apellido = datos_futbolista['apellido'], edad = datos_futbolista['edad'])
            futbolista.save()
            return redirect('Futbolistas')
    formulario = FutbolistasFormulario()
        
    return render(request, 'AppCoder/formulario_futbolista.html', {'formulario': formulario})

def lista_basquetbolistas(request):
    basquetbolistas = None
    error_nombre = None
    error_apellido = None
    error_triples = None
    if request.method =='GET':
        nombre = request.GET.get('nombre', '')
        apellido = request.GET.get('apellido','')
        triples = request.GET.get('triples',None)
        if nombre == '' and apellido == '' and triples == '' : #Se considera que si no introdujo ningún campo, está queriendo ver todos.
            basquetbolistas = Basquetbolista.objects.all()
        elif nombre: 
            if nombre.replace(' ','').isalpha():
                basquetbolistas = Basquetbolista.objects.filter(nombre = nombre)
            else:
                error_nombre = 'Debe ingresar un nombre válido'
        
        elif apellido:
            if apellido.replace(' ','').isalpha():
                basquetbolistas = Basquetbolista.objects.filter(apellido = apellido)
            else:
                error_apellido = 'Debe ingresar un apellido válido'
                
        elif triples:
            try: 
                triples = int(triples)
                basquetbolistas = Basquetbolista.objects.filter(triples = triples)
            except:
                error_triples = 'Debe ingresar una cantidad de triples válida'   
                         
    return render(request, 'AppCoder/lista_basquetbolistas.html', {'basquetbolistas': basquetbolistas, 'error_nombre': error_nombre, 'error_apellido': error_apellido, 'error_triples': error_triples})        

def crear_basquetbolista(request):
    if request.method == 'POST':
        formulario = BasquetbolistasFormulario(request.POST)
        
        if formulario. is_valid():
            datos_basquetbolista = formulario.cleaned_data
            basquetbolista = Basquetbolista(nombre = datos_basquetbolista['nombre'], apellido = datos_basquetbolista['apellido'], triples = datos_basquetbolista['triples'])
            basquetbolista.save()
            return redirect('Basquetbolistas')
    formulario = BasquetbolistasFormulario()
        
    return render(request, 'AppCoder/formulario_basquetbolista.html', {'formulario': formulario})
    
def lista_tenistas(request):
    tenistas = None
    error_nombre = None
    error_apellido = None
    error_titulos = None
    if request.method =='GET':
        nombre = request.GET.get('nombre', '')
        apellido = request.GET.get('apellido','')
        titulos = request.GET.get('titulos',None)
        if nombre == '' and apellido == '' and titulos == '' : #Se considera que si no introdujo ningún campo, está queriendo ver todos.
            tenistas = Tenista.objects.all()
        elif nombre: 
            if nombre.replace(' ','').isalpha():
                tenistas = Tenista.objects.filter(nombre = nombre)
            else:
                error_nombre = 'Debe ingresar un nombre válido'
        
        elif apellido:
            if apellido.replace(' ','').isalpha():
                tenistas = Tenista.objects.filter(apellido = apellido)
            else:
                error_apellido = 'Debe ingresar un apellido válido'
                
        elif titulos:
            try: 
                titulos = int(titulos)
                tenistas = Tenista.objects.filter(titulos = titulos)
            except:
                error_titulos = 'Debe ingresar una cantidad de títulos válida'   
                         
    return render(request, 'AppCoder/lista_tenistas.html', {'tenistas': tenistas, 'error_nombre': error_nombre, 'error_apellido': error_apellido, 'error_titulos': error_titulos})        

def crear_tenista(request):
    if request.method == 'POST':
        formulario = TenistasFormulario(request.POST)
        
        if formulario. is_valid():
            datos_tenista = formulario.cleaned_data
            tenista = Tenista(nombre = datos_tenista['nombre'], apellido = datos_tenista['apellido'], titulos = datos_tenista['titulos'])
            tenista.save()
            return redirect('Tenistas')
    formulario = TenistasFormulario()
        
    return render(request, 'AppCoder/formulario_tenista.html', {'formulario': formulario})

def contacto(request):
    return render(request, 'AppCoder/contacto.html', {})