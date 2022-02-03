# 대표값
from sys import stdin

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
ave = round(sum(a)/n)

min = 2147000000

for idx, x in enumerate(a):
    tmp = abs(x - ave)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1

print(ave, res)