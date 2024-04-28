import sys

def fatorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
    
for linha in sys.stdin:
    M, N = map(int, linha.split())
    print(fatorial(M) + fatorial(N))