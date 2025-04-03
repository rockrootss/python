# Identificación de anagramas

# Determine si dos palabras ingresadas son anagramas (contienen las mismas letras en diferente orden).

# Ejemplo de entrada y salida esperada:

    #Ingrese la primera palabra: amor
    #Ingrese la segunda palabra: roma
    #Son anagramas.

    # Ingrese la primera palabra: python
    # Ingrese la segunda palabra: java
    # No son anagramas.

word1 = input("Ingrese 1er palabra o 'FIN' para terminar: ").strip()           #strip elimina espacios
word2 = input("Ingrese 2da palabra o 'FIN' para terminar: ").strip()

while word1 != 'FIN' or word2 != 'FIN':
    if sorted(word1.lower()) == sorted(word2.lower()):           #ordeno las letras y las paso a minuscula asi matchean todas las letras.
        print("Son anagramas")
    else:
        print("No son anagramas")
    word1 = input("Ingrese 1er palabra o 'FIN' para terminar: ").strip()
    word2 = input("Ingrese 2da palabra o 'FIN' para terminar: ").strip()



