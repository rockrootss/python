# Valide un nombre de usuario con los siguientes criterios:

    #- Al menos 5 caracteres.
    #- Contiene al menos un número.
    #- Contiene al menos una letra mayúscula.
    #- Solo puede contener letras y números.

# Ejemplo de entrada y salida esperada:

    #- Ingrese un nombre de usuario: Gamer123
    #- El nombre de usuario es válido.
    #- Ingrese un nombre de usuario: gamer
    #- El nombre de usuario no cumple con los requisitos.

import string

upper = string.ascii_uppercase
number = string.digits
other = string.punctuation

username = input("Ingrese un nombre de usuario: ")
while username != 'FIN':
    has_upper = any(char in upper for char in username)         # Verifica si hay al menos una mayúscula
    has_digit = any(char in number for char in username)        # Verifica si hay al menos un número
    has_other = any(char in other for char in username)         # Verifica si hay al menos un carácter especial
    if len(username) >= 5 and has_upper and has_digit and not has_other:
        print(f"El usuario {username} es valido.")
    else:
        print(f"El usuario {username} no es valido")
    username = input("Ingrese un nombre de usuario: ")



# any verifica si hay al menos un dato que busco en un iterable y le da valor Boolean a la variable

