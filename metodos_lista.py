#creando una lista con list()
lista = list(["hola", "Raul", 35, 44, 65, 85, True])
lista2 = list([55, 33, 88, 66, 77, 11, 44, 45])
print (lista)

cantidad_elementos = len(lista)

#agregando elemento a la  lista, al final
lista.append ("jeajejeje")

#agregando elemento a la lista en una posiciòn
lista.insert(2,"tome tome")

#agregando varios elementos a lista osea otra lista.
lista.extend([2,False,2030])

print(lista)
#elimina un elemento de la lista segun la posicion indicada.

lista.pop(len(lista)-1)
lista.pop(-1) # elimina el ultimo

#elimina segun el valor ...busca el valor y lo elemina.
lista.remove(35)
print(lista)

#borra todos los elementos.
lista.clear()
print(lista)

#ordena los elementos de una lista
lista2.sort()
print(lista2)

#revierte el orden de la lista.
lista2.reverse()
print(lista2)

#busca en la lista
posicion_encontrada = lista2.index(88)
print(posicion_encontrada)
