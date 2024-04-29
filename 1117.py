import sys

notas = []
while True:
    n = float(input())

    if n < 0 or n > 10:
        print("nota invalida")
    else:
        notas.append(n)

    if len(notas) == 2:
        break

print(f"media = {(sum(notas) / len(notas)):.2f}")