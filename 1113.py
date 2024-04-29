import sys

while True:
    a, b = list(map(int, input().split(" ")))

    if a == b:
        break
    elif a < b:
        print("Crescente")
    else:
        print("Decrescente")
