

nombre= input("¿Cuál es tu nombre? ")
sexo = input("¿Cuál es tu sexo? (Responda con H o M) ")

if (sexo.upper()=='M'and nombre.upper()<'M') or (sexo.upper()=='H'and nombre.upper()>'N'):
    grupo="A"
else:
    grupo="B"

print("Tu grupo es: "+grupo)
