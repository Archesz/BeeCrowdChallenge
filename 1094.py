n = int(input())

cobaias = {
    "coelhos": 0,
    "ratos": 0,
    "sapos": 0,
    "pcoelhos": 0,
    "pratos": 0,
    "psapos": 0
}

for i in range(n):
    v, c = input().split(" ")
    v = int(v)

    if c == "C":
        cobaias["coelhos"] += v
    elif c == "R":
        cobaias["ratos"] += v
    elif c == "S":
        cobaias["sapos"] += v
    
total = sum(cobaias.values())
cobaias["pcoelhos"] = round(cobaias["coelhos"] * 100 / total, 2)
cobaias["pratos"] = round(cobaias["ratos"] * 100 / total, 2)
cobaias["psapos"] = round(cobaias["sapos"] * 100 / total, 2)

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {cobaias['coelhos']}")
print(f"Total de ratos: {cobaias['ratos']}")
print(f"Total de sapos: {cobaias['sapos']}")
print(f"Percentual de coelhos: {cobaias['pcoelhos']:.2f} %")
print(f"Percentual de ratos: {cobaias['pratos']:.2f} %")
print(f"Percentual de sapos: {cobaias['psapos']:.2f} %")