import math

n = int(input())

def checkPrime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(2, round(math.sqrt(n))):
            if n % i == 0:
                return False
        return True

for i in range(0, n):
    x = int(input())

    isPrime = checkPrime(x)

    if isPrime:
        print("Prime")
    else:
        print("Not Prime")