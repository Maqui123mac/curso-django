from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render 

#"""


# Create your views here.
def principal(request):
    
    return render(request,"contenido/principal.html")

def Cursos(request):
  
    return render(request,"contenido/cursos.html")
def Formulario(request):
   
    return render(request,"contenido/formulario.html")