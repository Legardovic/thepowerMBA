inputUsuario = input("Introduzca un año: ")
	
if int(inputUsuario) % 4 == 0 and (int(inputUsuario) % 100 != 0 or int(inputUsuario) % 400 == 0):
	print(inputUsuario+" es bisiesto")
else:
	print(inputUsuario+ " no es bisiesto")