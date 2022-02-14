# 최소힙
from sys import stdin
import heapq as hq

a = []
while True:
    n = int(stdin.readline())
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(hq.heappop(a))
    else:
        hq.heappush(a, n)