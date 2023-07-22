#Define la lista de entrada con los números desordenados
entrada_usuario = input("Ingresa los números separados por espacios: ")
numeros = [int(numero) for numero in entrada_usuario.split()]

# Separar los números pares e impares en listas diferentes
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

# Ordenar los números pares en orden ascendente y los números impares en orden descendente
pares.sort()
impares.sort(reverse=True)

# Unir las listas ordenadas para obtener el resultado final
resultado_final = pares + impares


# Imprimir la lista original ingresada por el usuario
print("Lista original:", numeros)

# Imprimir el resultado final
print("Lista con números pares en orden ascendente y números impares en orden descendente:", resultado_final)
print("Lista con números pares en orden ascendente:", pares.sort())
print("Lista con números pares en orden ascendente y números impares en orden descendente:", resultado_final)