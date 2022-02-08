# 침몰하는 타이타닉(그리디)
from sys import stdin
from collections import deque
n, limit = map(int, stdin.readline().split())
p = list(map(int, stdin.readline().split()))
p.sort()
p = deque(p)
cnt = 0
while p:
    if len(p) == 1:
        cnt += 1
        break
    if p[0] + p[-1] > limit:
        p.pop()
        cnt += 1
    else:
        p.popleft()
        p.pop()
        cnt += 1
print(cnt)