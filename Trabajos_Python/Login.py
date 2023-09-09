import random
import re

def generate_static_captcha():
    captcha_question = "Por favor, responde a la siguiente pregunta de CAPTCHA: ¿Cuál es la capital de Francia? "
    expected_answer = "Paris"
    return captcha_question, expected_answer

def validate_email(correo):
    return re.match(r'^[\w\.-]+@[\w\.-]+$', correo)

def validate_phone(telefono):
    return len(telefono) == 10 and telefono.isdigit()

def register_user():
    print("Registro de Usuario")
    nombre = input("Nombre: ")
    while True:
        correo = input("Correo electrónico: ")
        if not validate_email(correo):
            print("Correo inválido.")
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
        metodo_ingreso = input("¿Va a ingresar por Correo o Telefono? ").lower()
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
            captcha_question, expected_answer = generate_static_captcha()
            print(captcha_question)
            respuesta_usuario = input("Respuesta del CAPTCHA: ")
            
            if respuesta_usuario.lower() == expected_answer.lower():
                print(f"¡Bienvenido, {nombre}!")
                break
            else:
                print("Respuesta incorrecta. Inicio de sesión fallido.")
        else:
            print("Contraseña incorrecta. Inténtelo de nuevo")
            

print("Bienvenido")

while True:
    print("\nMenú del Usuario:")
    print("1. Registrarse")
    print("2. Iniciar Sesión")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        nombre, correo, telefono, contraseña = register_user()
    elif opcion == '2':
        if 'correo' in locals() and 'telefono' in locals() and 'contraseña' in locals():
            login_user(correo, telefono, contraseña)
        else:
            print("Primero debes registrarte.")
    elif opcion == '3':
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

