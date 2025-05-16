grupos = ['A', 'B', 'C']
alumnos_por_grupo = 6
total_dias = 5

registro_asistencias = dict.fromkeys(grupos, 0)

for dia_actual in range(total_dias):
    print(f"\nJornada {dia_actual + 1}:")
    for grupo in grupos:
        print(f"Grupo {grupo}:")
        for num_alumno in range(1, alumnos_por_grupo + 1):
            while True:
                presente = input(f"Alumno {num_alumno} asistió? (S/N): ").strip().upper()
                if presente in ['S', 'N']:
                    break
                print("Respuesta no válida. Por favor, escribe 'S' o 'N'.")
            if presente == 'S':
                registro_asistencias[grupo] += 1

print("\nConteo de asistencias por grupo:")
acumulado = 0
for grupo, cantidad in registro_asistencias.items():
    print(f"Grupo {grupo}: {cantidad} asistencias")
    acumulado += cantidad

print(f"\nAsistencia total registrada en los {total_dias} días: {acumulado}")
