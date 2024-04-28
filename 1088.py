lista = [5, 1, 2, 3, 4, 5]

# Procurar o menor numero
def findSmall(lista):
    v = min(lista)
    min_index = lista.index(v)

    return min_index

def change(lista, smallest):
    if smallest != 0:
        if lista[smallest] < lista[smallest - 1]:
            lista[smallest], lista[smallest - 1] = lista[smallest - 1], lista[smallest]

    return lista

print(lista)
min_index = findSmall(lista)
lista = change(lista, min_index)
print(print(lista))
min_index = findSmall(lista)
lista = change(lista, min_index)
print(print(lista))
min_index = findSmall(lista)
lista = change(lista, min_index)
print(print(lista))
min_index = findSmall(lista)
lista = change(lista, min_index)
print(print(lista))
