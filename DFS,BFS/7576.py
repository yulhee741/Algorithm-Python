# 토마토
from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())

graph = [list(map(int, stdin.readline().split())) for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()

def bfs():
    cnt = 0

    while q:
        cnt += 1 # 일 증가

        for _ in range(len(q)):
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < m and 0 <= ny < n:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = 1
                        q.append([nx, ny])

    for i in range(len(graph)):
        if 0 in graph[i]:
            return -1
    
    return cnt -1


for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            q.append([i,j])

print(bfs())

