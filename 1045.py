lista = sorted(list(map(float, input().split(" "))))
lista.reverse()
a, b, c = lista[0], lista[1], lista[2]

if a >= b + c:
    print("NAO FORMA TRIANGULO")
else:
    if a**2 == b**2 + c**2:
        print("TRIANGULO RETANGULO")

    if a**2 > b**2 + c**2:
        print("TRIANGULO OBTUSANGULO")

    if a**2 < b**2 + c**2:
        print("TRIANGULO ACUTANGULO")

    if a == b and a == c:
        print("TRIANGULO EQUILATERO")

    if a == b and a != c or b == c and b != a:
        print("TRIANGULO ISOSCELES")