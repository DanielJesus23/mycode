
def obtener_dia(numero_dia):
    dias = {
        0: "Domingo",
        1: "Lunes",
        2: "Martes",
        3: "Miercoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sadabo",
    }
    return dias.get(numero_dia, "null")

disec = int(input("Ingrese un numero de los dias de la semana: "))
print(obtener_dia(disec))
if (disec > 5):
        if(disec!=0):
            print("Has elegido un dia de descando")
else:
    print("no es un dia de trabajo")    

numero1 = int(input("Dígame un número: "))
numero2 = int(input(f"Dígame un número mayor que {numero1}: "))
print(f"La diferencia entre ellos es {numero2 - numero1}.")

apert = (input("Ingrese su nombre: " ))
print (f"Hola {apert} Tienes {numero2 - numero1} anios")

#Ahora con numeros Reales
numflo1 = Double(input("Ingrese un numero de un dia de la semana"))
numflo2 = Double(input(f"Digite un numero de la semana diferente al {numflo1}"))
