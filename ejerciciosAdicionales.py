# vicky arteaga
# -------------------
# ---- Ejercicio 1
# Escriba una función que tome una lista de números y devuelva la suma acumulada,
# es decir, una nueva lista donde el primer elemento es el mismo, el segundo elemento
# es la suma del primero con el segundo, el tercer elemento es la suma del resultado
# anterior con el siguiente elemento y así sucesivamente. Por ejemplo, la suma acumulada
# de [1,2,3] es [1, 3, 6].
# -------------------

def sumarLista():
    lista1 = [1, 2, 3]
    suma = 0
    for i in lista1:
        suma = suma + i
        print(suma)


sumarLista()


# Ejercicio 2
# Escribe una función llamada "elimina" que tome una lista y elimine el primer y
# último elemento de la lista y cree una nueva lista con los elementos que no fueron
# eliminados.
# Luego escribe una función que se llame "media" que tome una lista y devuelva una nueva
# lista que contenga todos los elementos de la lista anterior menos el primero y el último.


def eliminar():
    lista2 = [1, 2, 3, 4, 5, 6, 7]
    lista2.pop(0)
    lista2.pop(len(lista2) - 1)
    return lista2


def media(lista2):
    print(lista2)


media(eliminar())


# version 2

def eliminar(lista5):

    lista5.pop(0)
    lista5.pop(len(lista5) - 1)
    return lista5


def media(lista4):
    print(lista4)


lista3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
media(eliminar(lista3))
