"""age = 10

height = 119

if height < 120 and age <= 10:
    print("Puede ingresar")

age = 19 

height = 145

if age > 17 or height > 150:
    print("Puede ingresar")

pay = int(input("Valor a pagar"))

print(type(pay))

print("El valor recibido fue de ", pay)"""

products = {
    "Producto 1": 10000,
    "Producto 2": 15000,
    "Producto 3": 20000,
    "Producto 4": 25000,
}

while True:
    print("Lista de productos:")
    for product, price in products.items():
        print(f"- {product}: ${price}")
    
    selected_products = []
    total_value = 0

    while True:
        product_choice = input("Seleccione un producto de la lista (ingrese el número) o presione Enter para finalizar: ")
        if product_choice == "":
            break
        
        product_index = int(product_choice) - 1
        product_names = list(products.keys())
        
        if 0 <= product_index < len(product_names):
            selected_product = product_names[product_index]
            selected_products.append(selected_product)
            total_value += products[selected_product]
            print(f"Producto seleccionado: {selected_product}")
        else:
            print("Selección inválida. Intente nuevamente.")

    if selected_products:
        print("Productos seleccionados:")
        for product in selected_products:
            print(f"- {product}")
        print(f"Valor total a pagar: ${total_value}")

        op = input("¿Desea incluir el servicio? (Y / N): ")
        if op == "Y":
            total_value += total_value * 0.1

        print("El valor a pagar es:", total_value)
    else:
        op2 = input("¿Desea hacer otro pedido? (Y / N): ")
        if op2 == "N":
            print("Gracias por su visita. ¡Hasta luego!")
            break