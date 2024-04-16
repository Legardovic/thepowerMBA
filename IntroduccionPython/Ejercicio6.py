inputUsuario = input("Introduzca una palabra: ")

if inputUsuario == inputUsuario[::-1]:
    print("Es palindromo.")
else:
    print("No es palindromo.")
    