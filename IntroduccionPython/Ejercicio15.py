
inputUsuario = input("Introduzca un número a convertir: ")


minutos = int(float(inputUsuario) % 60)
horas = int(float(inputUsuario) / 60)

print("Horas "+str(horas)+" min "+str(minutos))