# Modifique el ejercicio 4 para que dada la lista de número genere dos nuevas
# listas, una con los número pares y otras con los que son impares. Imprima
# las listas al terminar de procesarlas.

numerosP = []
numerosI = []
while True:

    entrada = (input("Ingrese un numero para agregar a la lista o 'fin para continuar': "))
    try:
        if entrada.lower() == 'fin':
            break
        numero = int(entrada)
        if numero % 2 == 0:
            numerosP.append(numero)
        else:
            numerosI.append(numero)    
    except ValueError:
        print("Por favor, ingresa un número válido o 'fin' para terminar.")

print("Los numeros pares ingresados son: ", numerosP)
print("Los numeros impares ingresados son: ", numerosI)