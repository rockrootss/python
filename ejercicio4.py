import random
# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]

# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
    "// Esto es un comentario",
    "/* Esto es un comentario */",
    "-- Esto es un comentario",
    "# Esto es un comentario",
),
("=", "==", "!=", "==="),
]

# Índice de la respuesta correcta para cada pregunta, en el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

# Convierto listas en tupla
questions_to_ask = random.sample(list(zip(questions, answers, correct_answers_index)), k=3)

puntaje = 0

# El usuario deberá contestar 3 preguntas
for question, answers, correct_answers_index in questions_to_ask:

# El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        # Mostrar la pregunta y las opciones numeradas
        print(f"\n{question}")                                           # Pregunto y "\n" SALTO DE LINEA              
        for i, ans in enumerate(answers):
            print(f"{i + 1}. {ans}")
        try:    
            user_answer = int(input("Respuesta: ")) - 1
# Si el valor que se ingresa es invalido, corto el programa.
        except ValueError:
            print("Respuesta invalida.")
            exit(1)
# Se verifica si los valores son validos
        if user_answer < 0 or user_answer > 3:
            print("Respuesta invalida.")
            exit(1)       
# Se verifica si la respuesta es correcta, sino descuento 0.5 al puntaje          
        if user_answer == correct_answers_index:
            print("¡Correcto!")
            puntaje += 1
            break
        else:
            puntaje -= 0.5
    else:
# Si el usuario no responde correctamente después de 2 intentos,
# se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(answers[question_index][correct_answers_index])

# Se imprime un blanco al final de la pregunta
print()

# Informo el puntaje del jugador
if puntaje < 0:
    print("Puntaje: 0")
else:
    print(f"Puntaje: {puntaje}")
