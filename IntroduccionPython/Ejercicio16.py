inputUsuario = input("Ingrese una lista de números separados por comas (ej 1,2,3,4): ")
inputLista = list(inputUsuario.replace(",",""))

sumaPar = 0
sumaImpar = 0
for i in range(0,len(inputLista)):
    if int(inputLista[i]) % 2 == 0: 
        sumaPar += 1
    else:
        sumaImpar += 1

print(" Hay "+str(sumaPar)+" números pares \n Hay "+str(sumaImpar)+" números impares")