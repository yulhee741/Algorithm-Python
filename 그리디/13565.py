# 침투
from sys import stdin
from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 2
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < m) and (0 <= ny < n) and graph[nx][ny] == 0:
                q.append((nx, ny))
                graph[nx][ny] = 2

m, n = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().rstrip())) for _ in range(m)]
dx = [-1, 1, 0 , 0]
dy = [0, 0, -1, 1]

for i in range(n):
    if graph[0][i] == 0:
        bfs(0, i)


if 2 in graph[-1]:
    print("YES")
else:
    print("NO")