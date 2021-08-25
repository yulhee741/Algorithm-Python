# 토마토
from sys import stdin
from collections import deque

m,n,h = map(int, stdin.readline().split())

graph = [[list(map(int, stdin.readline().split())) for _ in range(n)] for _ in range(h)]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
q = deque()

def bfs():
    cnt = 0

    while q:
        cnt += 1 # 일 증가

        for _ in range(len(q)):
            z, x, y = q.popleft()

            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]

                if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                    if graph[nz][nx][ny] == 0:
                        graph[nz][nx][ny] = 1
                        q.append([nz, nx, ny])

    for i in graph:
        for j in i:
            if 0 in j:
                return -1
    
    return cnt -1


for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                q.append([i,j,k])

print(bfs())

