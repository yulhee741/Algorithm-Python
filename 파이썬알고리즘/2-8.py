# 곳감(모래시계)
from sys import stdin

n = int(stdin.readline())

a = [list(map(int, stdin.readline().split())) for _ in range(n)]
m = int(stdin.readline())
for i in range(m):
    h, t, k = map(int, stdin.readline().split())
    if t == 0:
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))
    else:
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop())

res = 0
s = 0
e = n-1
for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(res)