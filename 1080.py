valores = []

for i in range(0, 100):
    valores.append(int(input()))

print(max(valores))
print(valores.index(max(valores)) + 1)