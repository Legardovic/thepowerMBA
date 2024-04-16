inputUsuario = input("Introduzca el monto de la cuenta: ")
inputMonto = float(inputUsuario)

montoTotal = round(inputMonto * 1.15, 2)

print("El monto total a pagar incluyendo la propina es: "+str(montoTotal))