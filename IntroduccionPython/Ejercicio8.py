inputPeso = input("Introduzca su peso en KG: ")
inputEstatura = input("Introduza su estatura en metros (ej 1.70): ")


IMC = round(float(inputPeso) / (float(inputEstatura)**2), 2)

print("Tu IMC es: "+str(IMC))