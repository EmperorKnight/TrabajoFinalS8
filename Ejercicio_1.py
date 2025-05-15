# Definir las variables iniciales 
secciones = 3 # Tres secciones 
estudiantes_por_seccion = 6 # Seis estudiantes por sección
dias = ["Lunes","Martes","Miercoles","Jueves","Viernes"] # Dias de la semana

# Inicializamos el contador de asistencias totales
asistencias_totales = 0

# Bucle para cada sección 
for seccion in range(1,secciones+1):
    print(f"\nSección {seccion}")
    asistencia_seccion = 0

    # Bucle para cada estudiante en la sección
    for estudiante in range(1,estudiantes_por_seccion+1):
        asistencia_estudiante = 0
        
        # Bucle de asistencia por dia
        for dia in dias:
            asistencia = input(f"¿El estudiante {estudiante} asistio el {dia}? (S/N): ").strip().upper()

            if asistencia == "S":
                asistencia_estudiante += 1
                asistencia_seccion += 1
                asistencias_totales += 1 # Incrementar el total de asistencias

        # Mostrar la asistencia de cada estudiante
        print(f"El estudiante {estudiante} tuvo {asistencia_estudiante} asistencias esta semana")

    # Mostrar la asistencia total de la seccion
    print(f"\nTotal de asistencias en la sección {seccion}: {asistencia_seccion}")

# Mostrar el total general de asistencias
print(f"\nTotal general de asistencias: {asistencias_totales}")