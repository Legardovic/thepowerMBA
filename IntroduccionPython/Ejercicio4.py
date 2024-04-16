inputUsuario = input("Introduzca una palabra: ")

def contar_vocales(palabra):
    vocales = 0
    for c in palabra:
        if c in "aeiouAEIOU":
            vocales += 1
    return vocales

contVocales = contar_vocales(inputUsuario)

print("La palabra "+inputUsuario+" tiene "+str(contVocales)+" vocales")