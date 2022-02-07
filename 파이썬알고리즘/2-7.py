# 사과나무(다이아몬드)
from sys import stdin

n = stdin.readline()
a = [list(map(int, stdin.readline().split())) for _ in range(n)]

res = 0
s = e = n//2
for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
         
print(res)