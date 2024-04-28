def checkLeap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

years = []
while True:
    try:
        year = int(input())
        years.append(year)
    except EOFError:
        break

for i in range(0, len(years)):
    year = years[i]

    if checkLeap(year) and year % 55 == 0:
        print("This is bulukulu festival year.")
    elif year % 15 == 0:
        print("This is huluculu festival year.") 
    elif checkLeap(year):
        print("This is leap year.")
    else:
        print("This is an ordinary year.")

    if i != len(years) - 1:
        print("")