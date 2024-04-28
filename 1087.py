coords = list(map(int, input().split(" ")))

while coords != [0, 0, 0, 0]:
    x1 = coords[0]
    x2 = coords[2]
    y1 = coords[1]
    y2 = coords[3]

    movs = 0
    if abs(x1 - x2) == abs(y1 - y2) and x1 != x2 and y1 != y2:
        movs += 1
    else:
        if x1 < x2 or x1 > x2:
            movs += 1

        if y1 < y2 or y1 > y2:
            movs += 1
        
    print(movs)

    coords = list(map(int, input().split(" ")))