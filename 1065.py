v1 = float(input())
v2 = float(input())
v3 = float(input())
v4 = float(input())
v5 = float(input())

counts = 0
valores = [v1, v2, v3, v4, v5]

for v in valores:
    if v % 2 == 0:
        counts += 1

print(f"{counts} valores pares")