# 사과나무
from sys import stdin

n = int(stdin.readline())

h = list(map(int, stdin.readline().split()))

d = 0
r = 0

for i in h:
    d += i // 2
    r += i % 2

if (d-r) % 3 == 0 and d >= r:
    print("YES")
else:
    print("NO")