# Escribe un programa que tome una lista de números enteros como entrada
# del usuario. Luego, convierte cada número en la lista a string y únelos en
# una sola cadena, separados por guiones ('-'). Sin embargo, excluye cualquier
# número que sea múltiplo de 3 de la cadena final.

numeros = []

while True:

    entrada = (input("Ingrese un numero o escriba 'fin' para continuar: "))
    try:
        if entrada.lower() == 'fin':                
            break
        numero = int (entrada)
        numeros.append(numero)
    except ValueError:
        print("Ingresar un valor correcto.")

cadena = ''

for i,num in enumerate(numeros):   #el numero en la pos i de la lista es num  
    numeros[i] = str (num)
    if num % 3 != 0:
        cadena += (f'-{numeros[i]}')

print(f'Los numeros son: {cadena}')

#cadena = '-'.join(str(n) for n in numeros if n % 3 != 0)
#print(cadena)


