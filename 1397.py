n = int(input())

while n != 0:
    p1 = 0
    p2 = 0

    for i in range(n):
        values = list(map(int, input().split(" ")))
        v1, v2 = values[0], values[1]

        if v1 > v2:
            p1 += 1
        elif v1 < v2:
            p2 += 1

    print(p1, p2)

    n = int(input())