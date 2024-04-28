class Fila():

    def __init__(self, notas, na):
        self.fila = notas
    
    def ordenarAlunos(self):
        notas = self.fila
        copy = notas.copy()

        for i in range(0, len(notas)):
            for j in range(0, len(notas) - 1):
                if notas[j] < notas[j+1]:
                    notas[j], notas[j+1] = notas[j+1], notas[j]
                    
        count = 0
        
        for i in range(0, len(notas)):
            if notas[i] == copy[i]:
                count += 1
        
        self.inalterados = count

    def exibir(self):
        print(self.fila)

n = int(input())

for i in range(0, n):
    na = int(input())
    notas = list(map(int, input("").split(" ")))
    fila = Fila(notas, na)
    fila.ordenarAlunos()
    print(fila.inalterados)