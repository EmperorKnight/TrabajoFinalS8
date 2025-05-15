import os

# Inicializamos variables
edificios = 4 # Cantidad de edificios
dias = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"] # Dias de la semana
total_por_edificio = [] # Guardado del consumo de cada edificio en la semana
total_semana = 0 # Total de la semana

# Bucle para cada edificio
for edificio in range(1,edificios+1):
    os.system("cls || clear")
    total_edificio = 0
    # Bucle por dia
    for dia in dias:
        print(f"Introduzca el consumo de enegia en kilovatios del edificio {edificio} del dia {dia}")
        turno_mañana = float(input(f"Turno de la mañana: "))
        turno_tarde = float(input(f"Turno de la tarde: "))
        turno_nocturno = float(input(f"Turno de la noche: ")) # Pedir cada turno
        print(" ") # Dejar un espacio despues del enter

        total_edificio += turno_mañana + turno_tarde + turno_nocturno # Suma de cada turno para obtener total de la semana del edificio
    
    total_por_edificio.append(str(total_edificio)) # Guardar el total del edificio
    total_semana += total_edificio # Total de la semana en general de cada edificio

promedio_semana = total_semana / edificios # Se obtiene el promedio la semana

# Imprimir
os.system("cls || clear")
print("--------------------------------------------------------------")
print(f"El promedio de la semana es de: {promedio_semana:,}kW")
print(f"El total de la semna es de: {total_semana:,}kW")
print("--------------------------------------------------------------")

x = ""
m = 1
for x in total_por_edificio:
    print(f"El consumo total de la semana del edificio {m} es de: {x}kW")
    m += 1

print("--------------------------------------------------------------")