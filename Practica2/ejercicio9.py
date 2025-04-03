#Limpieza de Datos para un Sistema de Clientes
    
    #Eres un analista de datos en una empresa que ha recibido una lista de nombres de clientes
    #de distintas fuentes.
    #Sin embargo, estos datos contienen errores, espacios en blanco, nombres repetidos y
    #valores nulos.
    #Tu tarea es desarrollar un sistema que limpie y estandarice estos datos para poder usarlos
    #en el sistema de facturación.
    #Datos de entrada
    #La empresa ha recopilado nombres de clientes desde diferentes formularios, bases de datos
    #y registros manuales.
    #La lista de datos inicial es la siguiente:

#clients = [
# " Ana López ", "Pedro Gómez", "maria martínez", "Pedro Gómez ", "",
# " Luis Rodríguez ", None, "ana lópez", "JUAN PÉREZ", "MARTA SUÁREZ",
# "luis rodríguez", "maría martínez ", " claudia torres", "CLAUDIA
# TORRES",
# " ", "pedro gómez", "Juan Pérez", None, "Ricardo Fernández", "LAURA
# RAMOS",
# "carlos mendes", "RICARDO FERNÁNDEZ ", " Laura ramos", "CARLOS MENDES",
# "alejandro gonzález", " ALEJANDRO GONZÁLEZ ", "Patricia Vega",
# "patricia VEGA", "Andrés Ocampo", " andrés ocampo", "Monica Herrera",
# "MONICA HERRERA ", "gabriela ruíz", "Gabriela Ruíz", "sandra morales",
# "SANDRA MORALES", "miguel ángel", "Miguel Ángel ", " Damián Castillo",
# "Damián Castillo ", None, "", " "
# ]

# es desarrollar un sistema que permita realizar las siguientes operaciones en los datos:

# Eliminar espacios extra en los nombres.
# Convertir todos los nombres a formato de título (primera letra en mayúscula y el
# resto en minúscula).
# Eliminar registros duplicados para evitar clientes repetidos.
# Eliminar valores vacíos o nulos, ya que no aportan información válida.
# Mostrar la lista limpia de clientes listos para usar en el sistema de facturación.

# Salida esperada
# Después de ejecutar las funciones de limpieza, la lista de clientes debería verse así:

#Lista limpia de clientes al realizar todas las operaciones:

#['Alejandro González', 'Ana López', 'Andrés Ocampo', 'Carlos Mendes',
# 'Claudia Torres', 'Damián Castillo', 'Gabriela Ruíz', 'Juan Pérez',
# 'Laura Ramos', 'Luis Rodríguez', 'Maria Martínez', 'Miguel Ángel',
# 'Monica Herrera', 'Patricia Vega', 'Pedro Gómez', 'Ricardo Fernández',
# 'Sandra Morales']

clients = [
" Ana López ", "Pedro Gómez", "maria martínez", "Pedro Gómez ", "",
" Luis Rodríguez ", None, "ana lópez", "JUAN PÉREZ", "MARTA SUÁREZ",
"luis rodríguez", "maría martínez ", " claudia torres", "CLAUDIA TORRES",
" ", "pedro gómez", "Juan Pérez", None, "Ricardo Fernández", "LAURA RAMOS",
"carlos mendes", "RICARDO FERNÁNDEZ ", " Laura ramos", "CARLOS MENDES",
"alejandro gonzález", " ALEJANDRO GONZÁLEZ ", "Patricia Vega",
"patricia VEGA", "Andrés Ocampo", " andrés ocampo", "Monica Herrera",
"MONICA HERRERA ", "gabriela ruíz", "Gabriela Ruíz", "sandra morales",
"SANDRA MORALES", "miguel ángel", "Miguel Ángel ", " Damián Castillo",
"Damián Castillo ", None, "", " "
]

clean_list = [client.strip() for client in clients if client and client.strip()]    # if cliente, filtra los valores 'none', ya que none es falso en python
                                                                                    # if cliente.strip, limpia los usuarios en blanco " " y los convierte en "" 
                                                                                    # que tambien se considera falso en python y los descarta





clean_list = [client.title() for client in clean_list]                        # .title() convierte a formato titulo, poniendo la primera letra en mayuscula

clean_list = set(clean_list)                                                  # La funcion set elimina los duplicados de la lista y lo convierte en conjunto
                                                                              # se puede volver a transformar en lista usando list(set(clean_list))

print(f"Lista limpia de clientes: {clean_list}")

# Tambien se podrian ordenar alfabeticamente con    clean_list = sorted(set(clean_list))
