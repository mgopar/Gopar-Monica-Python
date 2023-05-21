def area_circulo(radio):
    pi=3.1416
    return pi*radio**2

def volumen_cilindro(radio, altura):
    return area_circulo(radio)*altura

radio= float(input('Cuál es el radio del circulo?'))
altura= float(input('Cuál es la altura del cilindro?'))

print('El area del circulo es:', area_circulo(radio))
print('El volumen del cilindro es:', volumen_cilindro(radio, altura))