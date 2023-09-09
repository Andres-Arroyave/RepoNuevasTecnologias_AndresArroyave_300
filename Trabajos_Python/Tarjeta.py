def calcular_estado_cuenta(valor_compra, num_cuotas):
    saldo = valor_compra
    cuota_mensual = valor_compra / num_cuotas
    cupo_liberado = valor_compra

    print("Estado de Cuenta:")
    print(f"Valor de la Compra: ${valor_compra:.2f}")
    print(f"Número de Cuotas: {num_cuotas}")
    print("--------------------------------------------------")

    cuota_numero = 1
    while cuota_numero <= num_cuotas and saldo >= 0:
        saldo -= cuota_mensual
        print(f"Cuota {cuota_numero} - Cuota: ${cuota_mensual:.2f} | Saldo: ${saldo:.2f}")
        cuota_numero += 1

    print("--------------------------------------------------")
    print(f"Cupo Liberado: ${cupo_liberado:.2f}")

valor_compra = float(input("Ingresa el valor de la compra: "))
num_cuotas = int(input("Ingresa el número de cuotas: "))
calcular_estado_cuenta(valor_compra, num_cuotas)
