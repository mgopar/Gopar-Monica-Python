
import pandas as pd
notas = {'Juan':9, 'María':6.5, 'Pedro':4, 'Carmen':8.5, 'Luis':5}

def aprobados(notas):
    notas = pd.Series(notas)
    return notas[notas >= 6].sort_values(ascending=False)