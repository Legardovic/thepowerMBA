from datetime import datetime
from dateutil.relativedelta import relativedelta

inputUsuario = input("Introduzca su fecha de nacimiento (ej 1980/01/31): ")

fecha = datetime.strptime(inputUsuario, "%Y/%m/%d")
edad = relativedelta(datetime.now(), fecha)

print("Tiene "+str(edad.years)+" años")

