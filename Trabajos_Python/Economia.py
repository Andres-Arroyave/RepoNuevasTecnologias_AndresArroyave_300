transacciones = []
ingresos = {'Ingresos laborales': 0, 'Ingresos por renta': 0, 'Ingresos ocasionales': 0}
egresos = 0

def ingresar_dinero():
    global ingresos
    global transacciones
    tipo_ingreso = int(input("Tipo de ingreso:\n1. Ingresos laborales\n2. Ingresos por renta\n3. Ingresos ocasionales\nElija el tipo de ingreso: "))
    if tipo_ingreso in [1, 2, 3]:
        cantidad = float(input("Ingrese la cantidad: "))
        ingresos[list(ingresos.keys())[tipo_ingreso - 1]] += cantidad
        transacciones.append(f"Ingreso - {cantidad}")
        print("Ingreso registrado exitosamente.")
    else:
        print("Tipo de ingreso no válido.")

def retirar_dinero():
    global egresos
    global transacciones
    cantidad = float(input("Ingrese la cantidad a retirar: "))
    if cantidad <= sum(ingresos.values()) - egresos:
        egresos += cantidad
        transacciones.append(f"Egreso - {cantidad}")
        print("Retiro registrado exitosamente.")
    else:
        print("Fondos insuficientes para retirar esa cantidad.")

def mostrar_resumen():
    global ingresos
    global egresos
    global transacciones
    print("\nHistorial de transacciones:")
    for index, transaccion in enumerate(transacciones, start=1):
        print(f"{index}. {transaccion}")
    print("\nIngresos:")
    for tipo, cantidad in ingresos.items():
        print(f"{tipo}: {cantidad}")
    print(f"Egresos: {egresos}")
    saldo = sum(ingresos.values()) - egresos
    print(f"Saldo disponible: {saldo}")

while True:
    print("\nMenu:")
    print("1. Ingresar dinero")
    print("2. Retirar dinero")
    print("3. Mostrar resumen financiero")
    print("4. Salir")
    opcion = int(input("Elija una opción: "))

    if opcion == 1:
        ingresar_dinero()
    elif opcion == 2:
        retirar_dinero()
    elif opcion == 3:
        mostrar_resumen()
    elif opcion == 4:
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")
