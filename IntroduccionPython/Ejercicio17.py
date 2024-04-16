#Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendoque 1 milla equivale a 1.60934 kilómetros

def convMillasKM (millas):
    km = millas * 1.60934
    return km


inputUsuario = input("Introduzca la distancia en millas: ")

resultado = convMillasKM(float(inputUsuario))

print(inputUsuario+" millas son "+str(resultado)+" kilometros")