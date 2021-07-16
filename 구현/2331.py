# 반복 수열
from sys import stdin

a, p = stdin.readline().split()
d = [int(a), ]


while True:
    result = sum([int(i)**int(p) for i in a])
    if result not in d:
        d.append(result)
        a = str(result)
        result = 0
    else:
        idx = d.index(result)
        d = d[:idx]
        break
       

print(len(d))