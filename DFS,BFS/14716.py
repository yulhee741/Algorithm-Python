# 현수막
from sys import stdin
from collections import deque

m, n = map(int, stdin.readline().split())
graph = [list(map(int,stdin.readline().rstrip().split())) for _ in range(m)]
d = [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(y, x):
    q = deque()
    q.append((y,x))
    graph[y][x] = 0
    while q:
        y, x = q.popleft()
        for i in range(8):
            dx, dy = d[i][1], d[i][0] 
            nx, ny = dx + x, dy + y
            if 0 <= nx < n and 0 <= ny < m and graph[ny][nx] == 1:
                q.append((ny, nx))
                graph[ny][nx] = 0


cnt = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            bfs(i, j)
            cnt += 1

print(cnt)