n = int(input())

for i in range(0, n):
    x = float(input())

    days = 0
    
    while x > 1:
        x /= 2
        days += 1

    print(f"{days} dias")