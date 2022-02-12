# 응급실(큐)
from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
q = [(pos, val) for pos, val in enumerate(list(map(int, stdin.readline().split())))]
q = deque(q)
cnt = 0
while True:
    cur = q.popleft()
    if any(cur[1] < x[1] for x in q):
        q.append(cur)
    else:
        cnt += 1
        if cur[0] == m:
            print(cnt)
            break