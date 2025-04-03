# Generador de códigos de descuento

# Genere un código de descuento aleatorio para un usuario en base a su nombre, la fecha
# actual y el resto deben ser números o letras aleatorias. El código debe tener una longitud de
# 30 caracteres, todas las letras deben ser mayúsculas.
# El usuario debe ingresarse por teclado y debe validar que no exeda los 15 caracteres.

# Entrada:

    # Usuario: StreamerPro
    # Fecha: 2025-04-10

# Salida esperada:

    # Código de descuento: STREAMERPRO-20250410-AB12CDECA

import random
import string

user = input("Ingrese usuario(Menor a 15 caracteres) o 'FIN' para terminar: ").upper()
while user != 'FIN':
    if len(user) > 15:
        print("El usuario excede los 15 caracteres, intente otra vez")
        user = input("Ingrese usuario(Menor a 15 caracteres): ").upper()
    date = input("Ingrese fecha (YYYY-MM-DD): ").strip()
    date = date.replace("-","")

    code_len = 30 - (len(user) + len(date) - 2)           # Largo del codigo = 30 caracteres - (largo del usuario + largo de la fecha + 2)
    random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=code_len)) # Al usar''.join lo convierte en string, sino seria una lista. 
                                                                                                        # random.choices(secuencia, k=n) selecciona x elementos aleatorios con repetición de la secuencia.
    code = f'{user}-{date}-{random_part}'
    print(f"Codigo de descuento: {code}")

    user = input("Ingrese usuario(Menor a 15 caracteres) o 'FIN' para terminar: ").upper()


