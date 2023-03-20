#creando una lista (se pueden modificar)
lista = ["Lucas Dalto", "Soy Dalto", True, 1.85, "Soy Dalto"]

#creando una tupla (no se pueden modificar)
tupla = ("Lucas Dalto", "Soy Dalto", True, 1.85, "Soy Dalto")

#esto e valido
lista[3]="Maquinola"
#esto no
# tupla[3] ="Maquinola"

#creando un conjunto (set) (no se accede a elementos por indice, no se almacenan datos duplicados.)
conjunto = {"Lucas Dalto", "Soy Dalto", True, 1.85, "Soy Dalto"}

#print(conjunto[3]) -> no puede acceder al elemento 

#creando un diccionario (dict) (la estructura es key : value separados por coma)
diccionario = {
    'nombre' : "Lucas Dalto",
    'canal': "Soy Dalto",
    'esta emocionado': True,
    'altura':1.84,
    'dato_duplicado':"Soy Dalto"
}

print(diccionario['altura'])
print(lista[3])
print(tupla[3])

