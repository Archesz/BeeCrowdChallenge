v1 = float(input())
v2 = float(input())
v3 = float(input())
v4 = float(input())
v5 = float(input())

pares = 0
impares = 0
negativos = 0
positivos = 0
valores = [v1, v2, v3, v4, v5]

for v in valores:
    if v % 2 == 0:
        pares += 1
    else:
        impares += 1
    if v < 0:
        negativos += 1
    elif v > 0:
        positivos += 1

print(f"{pares} valor(es) par(es)")
print(f"{impares} valor(es) impar(es)")
print(f"{positivos} valor(es) positivo(s)")
print(f"{negativos} valor(es) negativo(s)")
