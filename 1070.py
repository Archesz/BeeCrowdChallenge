n = int(input())

if n % 2 != 0:
    print(n)
    for i in range(5):
        n += 2
        print(n)
else:
    n += 1
    print(n)
    for i in range(5):
        n += 2
        print(n)