n = int(input())

def ordenar(entry):
    entry = entry.split(" ")
    lista = []

    for item in entry:
        if item not in lista:
            lista.append(item)

    lista = sorted(lista)
    print(" ".join(lista))

for i in range(n):
    entry = input()
    ordenar(entry)