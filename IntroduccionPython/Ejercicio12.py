inputLongitud = input("Ingrese la longitud del rectángulo: ")
inputAncho = input("Ingrese el ancho del rectángulo: ")

def calcularArea (longitud, ancho):
    area = longitud * ancho
    return area

resultado = calcularArea(float(inputLongitud), float(inputAncho))

print("El área del rectángulo es: "+str(resultado))