class Pipa():
    def __init__(self, n):
        self.barbantes = None
        self.lados = n

    def calcularDiagonais(self):
        d = (self.lados * (self.lados - 3)) / 2
        self.barbantes = int(d)

n = int(input())

pipa = Pipa(n)
pipa.calcularDiagonais()
print(pipa.barbantes)