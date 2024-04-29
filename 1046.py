a, b = list(map(int, input().split(" ")))

if a == b:
    v = 24
elif a > b:
    v = 24 - a + b
else:
    v = b - a

print(f"O JOGO DUROU {v} HORA(S)")