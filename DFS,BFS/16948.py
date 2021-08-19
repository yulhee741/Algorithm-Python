# 데스 나이트
from sys import stdin
from collections import deque

n = int(stdin.readline().rstrip())
x, y, endx, endy = map(int, stdin.readline().split())

graph = [[0 for _ in range(n)] for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]


def bfs(a, b):
    graph[a][b] = 1
    visited[a][b] = 1

    q = deque()
    q.append((a,b))

    while q:
        now = q.popleft()
        x, y = now[0], now[1]
        
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if visited[nx][ny] == 1:
                continue

            visited[nx][ny] = 1
            graph[nx][ny] = graph[x][y] + 1
            q.append((nx,ny))


bfs(x, y)
print(graph[endx][endy]-1)