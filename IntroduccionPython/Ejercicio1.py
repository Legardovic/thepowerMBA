inputUsuario = input("Introduzca los grados en celsius: ")
inputCelsius = float(inputUsuario)

def conversorTemp (celsius):
    resultado = (celsius * 9 / 5) + 32 
    return resultado

farenheit = conversorTemp (inputCelsius)

print(inputUsuario+" grados celsius son "+str(farenheit)+" farenheit.")