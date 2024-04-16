def primo(num):
    for i in range(2, num):
        if num % i == 0:
            print("No es primo")
            return False
    print("Es primo")
    return True

inputUsuario = input("Introduza un número: ")

primo(int(inputUsuario))