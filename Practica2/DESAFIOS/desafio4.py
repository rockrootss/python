# Dada una lista de palabras, usando list comprehension generar otra lista con aquellos verbos en infinitivo.

list = ["dale", "leda", "desafio", "mate", "calate"]
print(f"list: {list}")
new_list = [pal for pal in list if pal.endswith("e")]
print(f"new_list: {new_list}")