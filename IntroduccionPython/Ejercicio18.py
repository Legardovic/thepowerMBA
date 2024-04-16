inputUsuario = input("Introduzca una frase: ")

inputLista = list(inputUsuario.split(" "))

contPalabras = len(inputLista)

print("En la frase hay "+str(contPalabras)+" palabras")