while True:
    x, y = list(map(int, input().split(" ")))

    if x == 0 or y == 0:
        break
    else:
        if x < 0 and y < 0:
            print("terceiro")
        elif x < 0 and y > 0:
            print("segundo")
        elif x > 0 and y > 0:
            print("primeiro")
        elif x > 0 and y < 0:
            print("quarto")