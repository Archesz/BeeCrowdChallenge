n = int(input())

lista = []
for i in range(n):
    x = int(input())
    lista.append(x)

y = 0
n = 0

for x in lista:
    if x >= 10 and x <= 20:
        y += 1
    else:
        n += 1

print(f"{y} in")
print(f"{n} out")