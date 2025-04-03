# Análisis de descripciones de una plataforma de stream

# Dadas varias descripciones de streams en Twitch, cuente cuántas menciones hay de
# "entretenimiento", "música" y "charla".

# Salida esperada:

    # Menciones de 'música': 4
    # Menciones de 'charla': 2
    # Menciones de 'entretenimiento': 1

descriptions = [
"Streaming de música en vivo con covers y composiciones",
"Charla interactiva con la audiencia sobre series y películas",
"Jugamos a juegos retro y charlamos sobre su historia",
"Exploramos la mejor música de los 80s y 90s",
"Programa de entretenimiento con noticias y curiosidades del mundo gamer",
"Sesión de charla con invitados especiales del mundo del streaming",
"Música en directo con improvisaciones y peticiones del chat",
"Un espacio para charlar relajada sobre tecnología y cultura digital",
"Exploramos el impacto de la música en los videojuegos clásicos"
]

musica = 0
charla = 0
entretenimiento = 0

for elem in descriptions:
    palabras = elem.split()                                             # Hago split para analizar palabra por palabra asi solo cuenta charla y no Charlar y charlaremos.
    musica += palabras.count('música') + palabras.count('Música')       # Analizo palabra por palabra con su variante iniciando en mayuscula ya que count no acepta 2 parametros
    charla += palabras.count('charla') + palabras.count('Charla')
    entretenimiento += palabras.count('entretenimiento') + palabras.count('Entretenimiento')

print(f"Veces que se menciono musica {musica}")
print(f"Veces que se menciono charla {charla}")
print(f"Veces que se menciono entretenimiento {entretenimiento}")



