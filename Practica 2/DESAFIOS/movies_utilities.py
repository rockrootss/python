

def input_movies():
    """ESTA FUNCION CREA UNA LISTA DE DURACION DE PELICULAS QUE SE INGRESAN POR TECLADO"""
    movies_duration = [] 
    min = int(input("Ingresar duracion de la pelicula o '0' para salir: "))
    while min != 0:
        movies_duration.append(min)
        min = int(input("Ingresar duracion de la pelicula: "))

    return movies_duration


def calc_average(movies):

    """ ESTA FUNCION CALCULA LA DURACION PROMEDIO DE LAS PELICULAS """

    len_movies = len(movies)

    average = 0 if len_movies == 0 else sum(movies) / len_movies

    return average




def max_average (movies,average):
    """ESTA FUNCION DEVUELVE CUANTAS PELICULAS SUPERAN EL PROMEDIO DE DURACION"""
    
    max = 0
    for elem in movies:
        if elem > average:
            max += 1
    
    print(f'{max} peliculas superan el promedio de duracion')


