numbers_lines = {"1": 2, "2": 5, "3": 5, "4": 4, "5": 5, "6": 6, "7": 3, "8": 7, "9": 6, "0": 6}

def countLed(entry):
    soma = 0
    for c in entry:
        soma += numbers_lines[c] 

    print(f"{soma} leds")

n = int(input())

for i in range(n):
    entry = input()
    countLed(entry)