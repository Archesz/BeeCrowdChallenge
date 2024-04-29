def convert(value_original):
    dic = {
        100: 0,
        50: 0,
        20: 0,
        10: 0,
        5: 0,
        2: 0,
        1: 0,
        0.50: 0,
        0.25: 0,
        0.10: 0,
        0.05: 0,
    }

    for value in dic.keys():
        while value_original >= value:
            value_original -= value
            dic[value] += 1
    # Moedas de 1 cent
    value_original = round(value_original, 2)
    count = 0
    while value_original >= 0.01:
        value_original = round(value_original - 0.01, 2)
        count += 1

    return dic, count

value = float(input())

dic, count = convert(value)
print("NOTAS:")
for key in dic.keys():
    if key > 1:
        print(f"{dic[key]} nota(s) de R$ {float(key):.2f}")

print("MOEDAS:")
for key in dic.keys():
    if key <= 1:
        print(f"{dic[key]} moeda(s) de R$ {float(key):.2f}")
print(f"{count} moeda(s) de R$ 0.01")