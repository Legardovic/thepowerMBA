def sumar (num1,num2):
    resultado = num1+num2
    return resultado

def restar (num1,num2):
    resultado = num1-num2
    return resultado

def multiplicar (num1,num2):
    resultado = num1*num2
    return resultado

def dividir (num1,num2):
    resultado = num1/num2
    return resultado

def askNums ():
    inputNum1 = input("Introduzca el primer número de la operación: ")
    inputNum2 = input("Introduzca el segundo número de la operación: ")
    return inputNum1, inputNum2

cont = True

while (cont):
    cont1 = True
    print("Elija la operación que quiere realizar: \n 1. Sumar\n 2. Restar \n 3. Multiplicar \n 4. Dividir \n 5. Salir \n")
    inputUsuario = input("Marque opción: ")

    match inputUsuario:
        case "1":
            inputNums = askNums()
            resultado = sumar(float(inputNums[0]),float(inputNums[1]))
            print("El resultado de la operación es: "+str(resultado))
        case "2":
            inputNums = askNums()
            resultado = restar(float(inputNums[0]),float(inputNums[1]))
            print("El resultado de la operación es: "+str(resultado))
        case "3":
            inputNums = askNums()
            resultado = multiplicar(float(inputNums[0]),float(inputNums[1]))
            print("El resultado de la operación es: "+str(resultado))
        case "4":
            inputNums = askNums()
            resultado = dividir(float(inputNums[0]),float(inputNums[1]))
            print("El resultado de la operación es: "+str(resultado))
        case "5":
            cont = False
            cont1 = False
        case _ :
            print("Opción incorrecta")
    while(cont1):
        inputOtra = input("Quiere realizar otra operación (S/N): ") 
        if inputOtra in "Nn":
            cont = False
            cont1 = False
        elif inputOtra in "Ss":
            cont1 = False
        else:
            print("Opción incorrecta")
        

        




