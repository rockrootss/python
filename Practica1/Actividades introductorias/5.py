# Implementa un programa que solicite al usuario que ingrese una lista de
# números. Luego, imprime la lista pero detén la impresión si encuentras un
# número negativo. Nota: utilice la sentencia break cuando haga falta.

numeros = []

while True:
    
    entrada = (input("Ingrese un numero o 'fin' para continuar: "))
    try:
        if entrada.lower () == 'fin':
            break
        numero = int(entrada)
        numeros.append(numero)    
    except  ValueError:
        print("Ingrese un numero valido.")

print("Los numeros ingresados son: ")

for numero in numeros:
    if numero < 0:
        break
    print(f"{numero}")
