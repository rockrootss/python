# Clasificación de velocidad de reacción en un juego

# Dado el tiempo de reacción de un jugador en milisegundos, clasifíquelo en las siguientes categorías:

    # Menos de 200 ms: Rápido
    # Entre 200 y 500 ms: Normal
    # Más de 500 ms: Lento

# Ejemplo de salida esperada:

    # Ingrese su tiempo de reacción en ms: 320
    # Categoría: Normal

time = int(input("Ingrese su tiempo de reaccion en ms: "))

while time != 0:
    if time < 200:
        print("Categoria: Rapido")
    elif time >= 200 and time <= 500:
        print("Categoria: normal")
    else: #time mayor que 500
        print("Categoria: Lento") 
    time = int(input("Ingrese su tiempo de reaccion en ms: "))    