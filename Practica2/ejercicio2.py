# Dado un listado de títulos de streams en Twitch:

""" titles = [
"Speedrun de Super Mario en tiempo récord",
"Charla sobre desarrollo de videojuegos",
"Jugando al nuevo FPS del momento con amigos",
"Música en vivo: improvisaciones al piano"
] """

#Encuentre el título con más palabras y muéstrelo en pantalla.

#Salida esperada:
    #El título más largo es: "Jugando al nuevo FPS del momento con amigos"

titles = [
"Speedrun de Super Mario en tiempo récord",
"Charla sobre desarrollo de videojuegos",
"Jugando al nuevo FPS del momento con amigos",
"Música en vivo: improvisaciones al piano"
]

longer = ""
for elem in titles:
    print(len(elem))
    if len(elem) > len(longer):
        longer = elem

print(longer)

