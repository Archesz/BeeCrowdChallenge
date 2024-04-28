import math

def distance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    d = round(dist, 4)
    return d

x1, y1 = list(map(float, input().split(" ")))
x2, y2 = list(map(float, input().split(" ")))

d = distance(x1, y1, x2, y2)
print(d)