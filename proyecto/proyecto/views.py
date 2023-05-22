from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect
import json

def index(request):
    return HttpResponse("Hola Mundo")

class VistaDatos(View):
    template_name ="portafolio.html"
    
    def post(self,request):
        return render(request)
    
    def get(self,request):
        nombre = "Monica"
        edad = 27
        genero = "femenino"
        cumpleaños = '9 de Julio'
        return render(request,self.template_name,{
            'nombre': nombre,
            'edad': edad,
            'genero': genero,
            'cumpleaños': cumpleaños
        })