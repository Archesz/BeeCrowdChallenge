def ordenar(strings):
    
    for i in range(len(strings)):
        string_list = strings[i].split(" ")
        
        for j in range(0, len(string_list)):
            for k in range(len(string_list) - 1):
                if len(string_list[k]) < len(string_list[k+1]):
                    string_list[k], string_list[k+1] = string_list[k+1], string_list[k]

        print(" ".join(string_list))

    return strings

n = int(input())
strings = []

for i in range(n):
    string = input()
    strings.append(string)

ordenar(strings)