# 결혼식
from sys import stdin
from collections import deque

n = int(stdin.readline())
m = int(stdin.readline())
friend = list([] for _ in range(n+1))

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    friend[a].append(b)
    friend[b].append(a)


def bfs(start):
    q = deque([[start, 0]])
    cnt = 0
    visited = [0 for _ in range(n+1)]
    visited[start] = 1
    while q:
        node, dist = q.popleft()
        if dist <= 2:
            cnt += 1
        for i in friend[node]:
            if not visited[i]:
                visited[i] = 1
                q.append([i, dist+1])
    return cnt-1

print(bfs(1))