from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect
import json


class Informacion(View):
    template_name ="cv.html"
    
    def post(self,request):
        return render(request)
    
    def get(self,request):
        datos = {'nombres':'Mónica Itzel', 'primer_apellido':'Gopar', 'segundo_apellido':'Méndez', 'fecha_nacimiento':'09/07/1996', 'celular': 3338209650, 'correo':'monica.goparm@gmail.com', 'domicilio':'Paseo del Sol 48, Col Mar', 'genero':'Femenino', 'objetivo': 'Seguir creciendo profesionalmente', 'salario_esperado': '$50,000.00'}
        skills = list(('Python','SQL', 'PLSQL','C++','Java','R'))
        trabajo = {'lugar_trabajo': ['CFE','Oracle'], 'anio_inicio': [2020, 2021], 'anio_fin': [2021, 'Presente'], 'puesto': ['Soporte','Senior developer'] }
        return render(request,self.template_name, {
            'nombres': datos["nombres"],
            'primer_apellido': datos["primer_apellido"],
            'segundo_apellido': datos["segundo_apellido"],
            'fecha_nacimiento': datos["fecha_nacimiento"],
            'celular': datos["celular"],
            'correo': datos["correo"],
            'domicilio': datos["domicilio"],
            'genero': datos["genero"],
            'objetivo': datos["objetivo"],
            'salario_esperado': datos["salario_esperado"],
            's0' : skills[0],
            's1' : skills[1],
            's2' : skills[2],
            's3' : skills[3],
            's4' : skills[4],
            's5' : skills[5],
            'lugar_trabajo1' : trabajo["lugar_trabajo"][0],
            'año_inicio1' : trabajo["anio_inicio"][0],
            'año_fin1' : trabajo["anio_fin"][0],
            'puesto1' : trabajo["puesto"][0],
            'lugar_trabajo2' : trabajo["lugar_trabajo"][1],
            'año_inicio2' : trabajo["anio_inicio"][1],
            'año_fin2' : trabajo["anio_fin"][1],
            'puesto2' : trabajo["puesto"][1]
        })