import datetime

def contar_vocales(frase):
	vocales = 0
	for letra in frase:
		if letra.lower() in "aeiou":
			vocales += 1
	return vocales

nombre= input("¿Cuál es tu nombre? ")
apellido1 = input("¿Cuál es tu primer apellido? ")
apellido2 = input ("¿Cuál es tu segundo apellido? ")
año = input("¿En que anio naciste? ")
mmdd = input("¿En que mes y dia naciste? (mm-dd) ")
año_actual = 2023
edad=año_actual-int(año)
ddmm=datetime.datetime.strptime(mmdd, '%m-%d').strftime('%d-%m')

print("")
print('Este es tu nombre en mayusculas: ',  (nombre+" "+apellido1+" "+apellido2).upper())
print('Este es tu nombre en minusculas: ',  (nombre+" "+apellido1+" "+apellido2).lower())
print('Tu fecha de nacimiento: ', ddmm+"-"+año)
print("Esta es tu edad", edad)
print("Tu nombre completo tiene", contar_vocales(nombre+apellido1+apellido2),"vocales.")
print("Tu nombre completo tiene", len(nombre+apellido1+apellido2),"letras.")
print("¿Tu edad es un carácter de tipo número?", type(edad)==int)
print("¿Tu nombre completo es un carácter de tipo alfanumérico?", type(nombre+apellido1+apellido2)==str)
print("Tu edad en 10 años será", edad+10)
print("La media de tu edad actual y tu edad en 20 años es", (edad+edad+10)/2)