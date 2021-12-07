# 경쟁적 전염
from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]
s, x, y = map(int, stdin.readline().split())

virus = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((graph[i][j], i, j))

virus.sort()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(S, X, Y):
    q = deque(virus)
    cnt = 0
    while q:
        if cnt == S:
            break

        for _ in range(len(q)):
            v, x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = graph[x][y]
                        q.append((graph[nx][ny], nx, ny))
        cnt += 1
    return graph[X-1][Y-1]

print(bfs(s, x, y))