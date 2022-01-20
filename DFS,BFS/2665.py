# 미로만들기
from sys import stdin
from collections import deque

n = int(stdin.readline().rstrip())

graph = [list(map(int, stdin.readline().rstrip())) for _ in range(n)]
visited = [[-1] * n for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    q = deque()
    q.append([0,0])

    visited[0][0] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == -1:
                    if graph[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append([nx,ny])
                    else:
                        visited[nx][ny] = visited[x][y]
                        q.appendleft([nx,ny])

bfs()
print(visited[n-1][n-1])