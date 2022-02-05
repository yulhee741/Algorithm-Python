# 카드 역배치
from sys import stdin

a = list(range(21))
for _ in range(10):
    s, e = map(int, stdin.readline())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i] = a[e-i], a[s+i] # 스와프
a.pop(0)
for x in a:
    print(x, end=' ')