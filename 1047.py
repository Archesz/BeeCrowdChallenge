a, b, c, d = map(int, input().split(" "))

if a == c and b == d:
    h = 24
    m = 0
else:
    if a <= c:
        h = c - a
    else:
        h = 24 - a + c
        
    if b <= d:
        m = d - b
    else:
        m = 60 - b + d
        h -= 1
        if h < 0:
            h = 24 + h

print(f"O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)")
