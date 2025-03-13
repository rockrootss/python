# Haz un programa que pida al usuario que ingrese una temperatura en
# grados Celsius y luego convierta esa temperatura a grados Fahrenheit,
# mostrando el resultado.

temp_celsius = int (input ("Ingrese temperatura en celsius: "))

temp_faren = (temp_celsius * 9/5) + 32

print(f"{temp_celsius}ºC = {temp_faren}ºF")