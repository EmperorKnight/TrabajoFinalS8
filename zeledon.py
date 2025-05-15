# Inicializamos estructura para guardar ventas
ventas = [[[0 for _ in range(3)] for _ in range(4)] for _ in range(3)]
# ventas[día][stand][producto]

# Ingreso de datos
for dia in range(3):
    print(f"\n--- Día {dia + 1} ---")
    for stand in range(4):
        print(f"\n  Stand {stand + 1}:")
        for producto in range(3):
            while True:
                try:
                    monto = float(input(f"    Ingrese monto de venta del Producto {producto + 1}: $"))
                    if monto < 0:
                        print("    El monto no puede ser negativo. Intente de nuevo.")
                        continue
                    ventas[dia][stand][producto] = monto
                    break
                except ValueError:
                    print("    Entrada inválida. Ingrese un número.")

# Mostrar resumen por stand, día y total general
total_general = 0

print("\n\n========== RESUMEN DE VENTAS ==========")
for dia in range(3):
    print(f"\n--- Día {dia + 1} ---")
    total_dia = 0
    for stand in range(4):
        total_stand = sum(ventas[dia][stand])
        total_dia += total_stand
        print(f"  Stand {stand + 1}: Total vendido = ${total_stand:.2f}")
    print(f"  Total del Día {dia + 1}: ${total_dia:.2f}")
    total_general += total_dia

print(f"\nTOTAL GENERAL DE LA FERIA: ${total_general:.2f}")