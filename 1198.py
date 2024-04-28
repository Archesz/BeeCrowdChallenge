while True:
    try:
        entrada = list(map(int, input().split(" ")))
        v = abs(entrada[0] - entrada[1])
        print(v)
    except EOFError:
        break
    
