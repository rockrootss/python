# Cree un programa que dada una lista de números imprima sólo los que son
# pares. Nota: utilice la sentencia continue donde haga falta.

numeros = []

while True:

    entrada = (input("Ingrese un numero para agregar a la lista o 'fin para continuar': "))
    try:
        if entrada.lower() == 'fin':
            break
        numero = int(entrada)
        numeros.append(numero)
    except ValueError:
        print("Por favor, ingresa un número válido o 'fin' para terminar.")

print("Los numeros ingresados son: ", numeros)