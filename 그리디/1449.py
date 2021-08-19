# 수리공 항승
from sys import stdin

n, l = map(int, stdin.readline().split())
points = list(map(int, stdin.readline().split()))
points.sort()

cnt = 0
tape = 0
for point in points:
    if tape < point:
        tape = point + l - 0.5
        cnt += 1

print(cnt)
