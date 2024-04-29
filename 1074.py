n = int(input())

valores = []

for i in range(n):
    valores.append(int(input()))

for i in valores:
    if i < 0 and i % 2 == 0:
        print("EVEN NEGATIVE")
    elif i < 0 and i % 2 != 0:
        print("ODD NEGATIVE")
    elif i > 0 and i % 2 == 0:
        print("EVEN POSITIVE")
    elif i > 0 and i % 2 != 0:
        print("ODD POSITIVE")
    elif i == 0:
        print("NULL")