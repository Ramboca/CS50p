cadena1 = "HolasoyRaul"
cadena2 = "Bienvenidos a programacion python."

# print (dir(cadena1)) muestra los posibles metodos
#convierte a mayusculas
resultado1 = cadena1.upper()

#convierte a minusculas
resultado1 = cadena1.lower()

#convierte primera letra a mayusculas
resultado2 = cadena2.capitalize()

print (resultado1)
print (resultado2)

#buscamos una cadena en otra cadena devuelve -1 cuando no lo encuentra.
busqueda_find = cadena1.find("a")
print(busqueda_find)
#buscamos una cadena en otra, si no la encuentra, nos manda una excepcion.
busqueda_index = cadena2.index("p")

#busca si es numerico
es_num = cadena1.isnumeric()
es_texto = cadena1.isalpha()
print(es_num, es_texto)


#cuenta las cantidad de veces que coincide.
contar_coincidencias = cadena2.count("d")
print(contar_coincidencias)

#contamos la cantidad de caracteres que tiene una cadena.
longitud = len(cadena2)
print(longitud)
# verificamos si una cadena empieza con ...una cadena.
empieza_con = cadena1.startswith("H")
finaliza_con = cadena2.endswith(".")

#reemplaza el pedazo de cadena por uno nuevo
cadena_nueva = cadena1.replace("Hola","hi, ")
print(cadena_nueva)

#separar cadenas con la cadena que le demos
cadena_separada = cadena2.split(" ")

print(cadena_separada)
