while True:
    n = int(input())
    if n == 0:
        break
    
    numbers = list(map(int, input().split()))  
    
    count = {}
    
    for num in numbers:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    for key, value in count.items():
        if value % 2 != 0:
            print(key)
            break