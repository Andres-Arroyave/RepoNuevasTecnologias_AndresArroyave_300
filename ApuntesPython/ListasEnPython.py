# Las listas son estructuras de datos lineales
# Se crean usando brackes ej: my 11st • [)
# las listas son ordenadas (Orden de insersion), esto quiere decir
# que el ultimo dato Ingresado ocupará la ultima posición.
# Emplea métodos para manipular los Items de la misma.
# Como los array la primera posicion Inicia en 0 permite Items duplicados.
# Las listas son mutables, es decir podemos agregar , actualizar o recover items
# Puede contener distintos tipos de datos

materias = ["Matematica", "Español " , "Ciencias", "Sociales", "Fisica", "Quimica"]

#Para deteminar el tamaño de la lista podemos usar len()
print(len(materias))

#print(dir(materias))

#Podemos acceder a los elementos indicando la posicion

print(materias[2])

#Slicing muestra las posiciones de un rango 

print(materias[2:5])

print(materias[3:])

print(materias[:5])

print(materias[-5:-1])
print(materias[1:5])


#Tipos de datos en las listas

edades = [17, 27, 42, 31, 56, 68]

print(type(edades))

#Actualizar un elemento de la lista 

materias[2] = "Biología"

print(materias[:])

materias[1:3] = "Lenguaje", "Ciencias Naturales"

print(materias[:])

#Agregando elementos a la lista

materias.append("Religión")
print(materias[:])

materias.insert(0, "Ética")
print(materias[:])


#Quitar elementos de la lista 

materias.pop()
print(materias[:])

materias.remove("Ética")
print(materias[:])

del materias[4]
print(materias[:])

# materias.clear()
# print(materias[:])

# del materias
# print(materias[:])

# Iterar las listas con el ciclo for



print("-"*50)

for i in materias:
    print(i)

print("-"*50)


for i in range(len(materias)):
    print(materias[i])

print("-"*50)

for i, materia in enumerate(materias):
    print(i, materia)

print("-"*50)


#Usando un ciclo while 

i = 0

while i < len(materias):
    print(materias[i])
    i += 1

print("-"*50)

#List Comprenhension

[print(i) for i in materias]

#Crear lista numero

numeros = [numero for numero in range(1,31)]

print(numeros)