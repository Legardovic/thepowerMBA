def convertirEURUSD (eur):
    usd = eur / 0.85
    return usd

def convertirUSDEUR (usd):
    eur = usd * 0.85
    return eur

cont = True
while(cont):
    cont1 = True
    print("Elija opción\n1. Convertir Euros a Dolares \n2. Convertir Dolares a Euros \n3. Salir")
    inputUsuario = input("Introduzca opción: ")
    match inputUsuario:
        case "1":
            inputQty = input("Introduca cantidad a convertir: ")
            resultado = convertirEURUSD(float(inputQty))
            print("Son "+str(resultado)+"$")
        case "2":
            inputQty = input("Introduca cantidad a convertir: ")
            resultado = convertirUSDEUR(float(inputQty))
            print("Son "+str(resultado)+"€")
        case "3":
            cont = False
            cont1 = False
        case _:
            print("Opción incorrecta")

    while(cont1):
        inputOtra = input("¿Quiere realizar otra conversión (S/N)?: ") 
        if inputOtra in "Nn":
            cont = False
            cont1 = False
        elif inputOtra in "Ss":
            cont1 = False
        else:
            print("Opción incorrecta")