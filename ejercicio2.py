# Definimos constantes para la estructura de los laboratorios
FILAS = 5
COLUMNAS = 4
LABORATORIOS = 2

# Función para crear un laboratorio con ingreso manual
def crear_laboratorio_manual(numero_lab):
    print(f"\n🔧 Ingreso manual del estado para el Laboratorio {numero_lab}")
    laboratorio = []
    for fila in range(FILAS):
        fila_computadoras = []
        for columna in range(COLUMNAS):
            while True:
                try:
                    estado = int(input(f"Ingrese estado para computadora en fila {fila + 1}, columna {columna + 1} (0 = libre, 1 = ocupada): "))
                    if estado in [0, 1]:
                        fila_computadoras.append(estado)
                        break
                    else:
                        print("⚠️ Solo se permite 0 (libre) o 1 (ocupada). Intenta de nuevo.")
                except ValueError:
                    print("⚠️ Entrada inválida. Debes ingresar 0 o 1.")
        laboratorio.append(fila_computadoras)
    return laboratorio

# Función para contar computadoras ocupadas y libres
def contar_computadoras(lab):
    ocupadas = 0
    libres = 0
    for fila in lab:
        for computadora in fila:
            if computadora == 1:
                ocupadas += 1
            else:
                libres += 1
    return ocupadas, libres

# Crear los laboratorios con ingreso manual
laboratorios = []
for i in range(1, LABORATORIOS + 1):
    laboratorio = crear_laboratorio_manual(i)
    laboratorios.append(laboratorio)

# Mostrar resultados
for i, lab in enumerate(laboratorios, start=1):
    print(f"\n📊 Estado del Laboratorio {i}:\n")
    
    # Mostrar la matriz con símbolos visuales
    for fila in lab:
        for computadora in fila:
            simbolo = "🟩" if computadora == 0 else "🟥"
            print(simbolo, end=" ")
print()

    # Mostrar resumen
ocupadas, libres = contar_computadoras(lab)
print(f"\nResumen del Laboratorio {i}:")
print(f"✅ Computadoras libres: {libres}")
print(f"❌ Computadoras ocupadas: {ocupadas}")