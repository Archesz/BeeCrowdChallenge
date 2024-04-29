n = int(input())

for i in range(0, n):
    a, b, c = list(map(float, input().split(" ")))
    m = (2 * a + 3 * b + 5 * c) / 10
    print(round(m, 1))