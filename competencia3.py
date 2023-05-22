

datos = {'nombres': 'Mónica Itzel', 
         'primer_apellido': 'Gopar', 
         'segundo_apellido':'Méndez', 
         'fecha_nacimiento':'09/07/1996',
         'celular':3338209650,
         'correo':'monica.goparm@gmail.com',
         'domicilio': 'Paseo del Sol 48, Col Mar',
         'genero': 'femenino',
         'objetivo': 'Seguir creciendo profesionalmente',
         'salario_esperado': '$50,00.00'}

skills=['Python','SQL', 'PLSQL', 'C++','Java','R']


trabajos = {'lugar_trabajo': ['CFE','Oracle'], 
            'anio_inicio': [2020, 2021], 
            'anio_fin': [2021, 'Presente'], 
            'puesto': ['Soporte','Senior developer'] }




for item in datos.items():
    print(item[0], ':', item[1])


for elemento in skills:
    print(elemento)

for item in trabajos.items():
    print(item[0], ':', item[1])
