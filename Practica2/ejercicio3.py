# Dado un código de conducta para un servidor de Discord:

"""
rules = Respeta a los demás. No se permiten insultos ni lenguaje
ofensivo.
Evita el spam. No publiques enlaces sospechosos o repetitivos.
No compartas información personal.
Usa los canales adecuados para cada tema.
Sigue las instrucciones de los moderadores.

"""

# Solicite una palabra clave al usuario e imprima todas las reglas que la contengan

rules = """ 
Respeta a los demás.
No se permiten insultos ni lenguaje ofensivo.
Evita el spam.
No publiques enlaces sospechosos o repetitivos.
No compartas información personal.
Usa los canales adecuados para cada tema.
Sigue las instrucciones de los moderadores.
"""

word =(input("Ingrese palabra para filtrar regla: "))

for lines in rules.split('.'):
    if word in lines.split():
        print(lines)

