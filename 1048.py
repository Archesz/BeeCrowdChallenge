n = float(input())

if n >= 0 and n <= 400.00:
    p = 15
elif n >= 400.01 and n <= 800.00:
    p = 12
elif n >= 800.01 and n <= 1200.00:
    p = 10
elif n >= 1200.01 and n <= 2000.00:
    p = 7
elif n > 2000.00:
    p = 4

r = round((n * p) / 100, 2)
new = n + r

print(f"Novo salario: {new:.2f}")
print(f"Reajuste ganho: {r:.2f}")
print(f"Em percentual: {p} %")