cont = True

while(cont):
    cont = False
    inputUsuario = input("Introduzca un número de día de un día la semana: ")
    match inputUsuario:
        case "1":
            print("Lunes")
        case "2":
            print("Martes")
        case "3":
            print("Miercoles")
        case "4":
            print("Jueves")
        case "5":
            print("Viernes")
        case "6":
            print("Sábado")
        case "7":
            print("Domingo")
        case "8":
            cont = False
        case _:
            print("Opción incorrecta")
            cont = True