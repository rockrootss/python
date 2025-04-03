# Ingresar palabras desde el teclado hasta ingresar la palabra FIN. Imprimir aquellas que empiecen y terminen con la misma letra.




word = input("Ingresa una palabra: ")
while word != 'FIN':
    if word[0] == word[-1]:
        print(f'{word} empieza y termina con la misma letra' )
    word = str(input("Ingresa una palabra: "))    

