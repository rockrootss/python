#Vamos a trabajar con las películas argentinas candidatas al premio Oscar a mejor película extranjera.
#Queremos saber:
#¿Cuál fue la duración promedio, en minutos, de todas las películas?
#¿Cuántas películas duran más que el promedio, en minutos?
longer = 0
duraciones = []

duration = int(input("Ingresar duracion de la pelicula: "))
while duration != 0:
    duraciones.append(duration)
    duration = int(input("Ingresar duracion de la pelicula: "))

promedio = sum(duraciones)/len(duraciones)

print(f'Promedio de duracion de todas las peliculas: {promedio}')

for elem in duraciones:
    if elem > promedio:
        longer += 1

print(f"Hay {longer} peliculas mas largas que la duracion promedio")