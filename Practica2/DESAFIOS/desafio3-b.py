#Vamos a trabajar con las películas argentinas candidatas al premio Oscar a mejor película extranjera.
#Queremos saber:
#¿Cuál fue la duración promedio, en minutos, de todas las películas?
#¿Cuántas películas duran más que el promedio, en minutos?

import DESAFIOS.movies_utilities as movies_utilities

movies = movies_utilities.input_movies()
average = movies_utilities.calc_average(movies)

print(movies)
print(average)
movies_utilities.max_average(movies,average)



