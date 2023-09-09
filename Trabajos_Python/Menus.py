import random
import re

def generate_captcha():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    captcha_question = f"¿Cuánto es {num1} {operator} {num2}? "
    expected_answer = eval(f"{num1} {operator} {num2}")
    return captcha_question, expected_answer

def validate_email(correo):
    return re.match(r'^[\w\.-]+@(gmail\.com|hotmail\.com)$', correo)

def validate_phone(telefono):
    return len(telefono) == 10 and telefono.isdigit()

def register_user():
    print("Registro de Usuario")
    nombre = input("Nombre: ")
    while True:
        correo = input("Correo electrónico: ")
        if not validate_email(correo):
            print("Correo inválido. Debe ser un correo de Gmail o Hotmail.")
        else:
            break
    while True:
        telefono = input("Teléfono: ")
        if not validate_phone(telefono):
            print("Número de teléfono inválido. Debe ser un número de 10 dígitos.")
        else:
            break
    while True:
        contraseña = input("Contraseña: ")
        if len(contraseña) < 8:
            print("La contraseña debe tener al menos 8 caracteres.")
        else:
            break
    
    print("Registro exitoso.")
    return nombre, correo, telefono, contraseña

def login_user(correo, telefono, contraseña):
    while True:
        metodo_ingreso = input("¿Va a ingresar por Correo  o Telefono? ").lower()
        if metodo_ingreso == "correo":
            correo_ingresado = input("Ingrese el Correo registrado: ")
            if correo_ingresado == correo:
                break
            else:
                print("Correo inválido. Intentelo de nuevo")
        elif metodo_ingreso == "telefono":
            telefono_ingresado = input("Ingresa el Telefono registrado: ")
            if telefono_ingresado == telefono:
                break
            else:
                print("Teléfono inválido. Inténtelo de nuevo")
        else:
            print("Opción inválida. Elige 'Correo' o 'Telefono'.")
    
    while True:
        contraseña_ingresada = input("Ingresa la contraseña: ")
        if contraseña_ingresada == contraseña:
            captcha_question, expected_answer = generate_captcha()
            print("Captcha:", captcha_question)
            respuesta_usuario = int(input("Respuesta del Captcha: "))
            
            if respuesta_usuario == expected_answer:
                print(f"¡Bienvenido, {nombre} !")
                break
            else:
                print("Captcha incorrecto. Inicio de sesión fallido.")
        else:
            print("Contraseña incorrecta. Inténtelo de nuevo")

print("Bienvenido")

while True:
    print("\nMenú:")
    print("1. Registrarse")
    print("2. Iniciar Sesión en la Cuenta")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        nombre, correo, telefono, contraseña = register_user()
    elif opcion == '2':
        if 'correo' in locals() and 'telefono' in locals() and 'contraseña' in locals():
            login_user(correo, telefono, contraseña)
            while True:
                print("\nMenú del Usuario:")
                print("1. Tarjeta de Crédito")
                print("2. Juego")
                print("3. Volver")
                
                opcion_usuario = input("Seleccione una opción: ")
                
                if opcion_usuario == '1':
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

                    valor_compra = float(input("Digite el valor de la compra: "))
                    num_cuotas = int(input("Digite el número de cuotas: "))
                    calcular_estado_cuenta(valor_compra, num_cuotas)
                elif opcion_usuario == '2':
                    import random

                    vidas = 5
                    puntos = 0

                    while vidas != 0:
                        num = random.randint(0, 9)

                        if num == 0:
                            vidas -= 1
                            print(f"Te quedan {vidas} vidas")
                        else:
                            puntos += 1
                            print(f"Has ganado {puntos} puntos")
                elif opcion_usuario == '3':
                    break
                else:
                    print("Opción inválida. Por favor, seleccione una opción válida.")
        else:
            print("Primero debes registrarte.")
    elif opcion == '3':
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")