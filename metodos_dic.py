diccionario = {
    "nombre" : 'Lucas',
    "apellido" : 'Marquez',
    "seguidores" : 1000000
}

# nos devuelve un objeto dict_item
usuarios = diccionario.keys()
print(usuarios)

# obtiene un elemento
usuarios = diccionario.get("nombre")
print(usuarios)

#eliminando un elemento del diccionario
diccionario.pop("seguidores")
print(diccionario)

#obteniendo un elemento dic_items iterac
diccionario_iterable = diccionario.items()
print(diccionario_iterable)


#eliminando todo el diccionario.
diccionario.clear()

print(diccionario)

