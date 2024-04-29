a = int(input())
b = int(input())

if a == b:
    print(0)
else:
    if a > b:
        lista = [x for x in range(b + 1, a) if x % 2 != 0]
    elif b > a:
        lista = [x for x in range(a + 1, b) if x % 2 != 0]

    print(sum(lista))