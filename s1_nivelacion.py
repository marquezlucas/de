#E1
while True:
    if int(input('Introduzca un número impar:'))%2==0:
        print('Incorrecto, introduzca un número impar')
    else:
        print('Ciclo finalizado')
        break

#E2
# Pedir al usuario cuántos números desea introducir
cantidad_numeros = int(input('introduzca la cantidad de numeros para hacer la media:'))

# Crear una lista para almacenar los números
numeros=[]

# Pedir al usuario que ingrese los números y agregarlos a la lista
for i in range(cantidad_numeros):
    num = float(input(f'Introduzca el número {i + 1}: '))  # Usamos float para permitir números decimales
    numeros.append(cantidad_numeros)
# Calcular la suma de los números
suma = sum(numeros)

# Calcular la media
media = suma / cantidad_numeros

# Imprimir la lista y la media
print(f'Lista de números ingresados: {numeros}')
print(f'Media aritmética: {media}')

#E3

#Todos los números del 0 al 10:
lista_1 = list(range(11))
#Todos los números del -10 al 0:
lista_2 = list(range(-10, 1))
#Todos los números pares del 0 al 20:
lista_3 = list(range(0, 21, 2))
#Todos los números impares entre -20 y 0:
lista_4 = list(range(-19, 1, 2))
#Todos los números múltiples de 5 del 0 al 50:
lista_5 = list(range(0, 51, 5))

print(lista_1)
print(lista_2)
print(lista_3)
print(lista_4)
print(lista_5)

#E4

def elementos_comunes(lista_1, lista_2):
    nueva_lista = list(set(lista_1).intersection(lista_2))
    return nueva_lista

# Ejemplo de uso:
lista_1 = ['l','u','c','a','s',' ','m','a','r','q','u','e','z']
lista_2 = ['h','o','l','a',' ','d','o','n']

resultado = elementos_comunes(lista_1, lista_2)
print(set(resultado))

#E5

# Inicializamos una variable para llevar la suma
suma_impares = 0

# Iteramos desde 0 hasta 100 (inclusive)
for i in range(101):
    if i % 2 != 0:  # Verificamos si el número es impar
        suma_impares += i  # Si es impar, lo sumamos a la variable

# Imprimimos el resultado
print(f"La suma de los números impares del 0 al 100 es: {suma_impares}")

#E6

# Definimos una lista
mi_lista = [1, 2, 3, 4, 1, 2, 1, 2, 3, 4, 5]

# Contamos cuántas veces aparece el número 1 en la lista
apariciones_de_1 = mi_lista.count(1)

# Contamos cuántas veces aparece el número 2 en la lista
apariciones_de_2 = mi_lista.count(2)

# Imprimimos los resultados
print(f"El número 1 aparece {apariciones_de_1} veces.")
print(f"El número 2 aparece {apariciones_de_2} veces.")


