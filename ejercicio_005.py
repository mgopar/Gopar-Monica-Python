tabla = {'Platano':1.35, 'Manzana':0.80, 'Pera':0.85, 'Naranja':0.70}
fruta = input('¿Qué fruta deseas? ').title()
if fruta in tabla:
    kilos = float(input('¿Cuántos kilos? '))
    print('Por', kilos, 'kilos de', fruta, 'serian', tabla[fruta]*kilos)
else: 
    print('Lo siento, por el momento no contamos con', fruta)