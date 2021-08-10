# 효율적인 해킹
from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[b].append(a)

def bfs(i):
    dq = deque()
    dq.append(i)
    visited = [0] * (n+1)
    visited[i] = 1
    cnt = 1

    while dq:
        now = dq.popleft()

        for i in graph[now]:
            if visited[i] == 0:
                visited[i] = 1
                dq.append(i)
                cnt += 1
    return cnt


mx = 0
result = []
for i in range(1, n+1):
    if graph[i]:
        cnt = bfs(i)
        if mx < cnt:
            mx = cnt
            result = [i]
        elif mx == cnt:
            result.append(i)

print(*result)
