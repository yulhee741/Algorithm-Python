# 창고 정리(그리디)
from sys import stdin

l = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
m = int(stdin.readline())

a.sort()
for _ in range(m):
    a[0] += 1
    a[l-1] -= 1
    a.sort()

print(a[l-1]-a[0])