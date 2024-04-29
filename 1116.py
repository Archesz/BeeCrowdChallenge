n = int(input())

for i in range(n):
    a, b = list(map(int, input().split(" ")))

    if b == 0:
        print("divisao impossivel")
    elif a == 0:
        print(0.0)
    else:
        print(a / b)