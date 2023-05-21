def longitud_frase(frase):
    return {palabra:len(palabra) for palabra in frase.split()}

frase = input('Escribe una frase: ').title()
print(longitud_frase(frase))