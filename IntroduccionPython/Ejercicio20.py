inputUsuario = input("Ingrese una lista de números separados por comas (ej 1,2,3,4): ")
inputLista = list(inputUsuario.replace(",",""))
suma = 0

for i in range(0,len(inputLista)):
    suma += int(inputLista[i]) 

print("Las suma de los números de la lista es: "+str(suma))