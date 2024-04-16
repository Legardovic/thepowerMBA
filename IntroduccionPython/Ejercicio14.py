#Crea un programa que calcule el precio final de un artículo después de aplicar un descuento del 20%.

def calcdescuento (precio):
    precioFinal = precio * 0.8
    return precioFinal

inputUsuario = input("Introduzca el precio del artículo: ")

resultado = calcdescuento(float(inputUsuario))

print("El precio final después de aplicar el descuento es: "+str(resultado))