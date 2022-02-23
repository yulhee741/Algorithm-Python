# 떡 먹는 호랭이
from sys import stdin

d, k = map(int, stdin.readline().split())

x, y = 1, 0
for i in range(d-1):
    x, y = y, x+y

for a in range(1, 100000):
    if (k-(a*x))%y == 0:
        print(a)
        print((k-(a*x))//y)
        break

