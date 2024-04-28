intervals = list(map(int, input().split(" ")))
s = ((intervals[1] - intervals[0] + 1) / 2) * (intervals[0] + intervals[1])
 
print(s)