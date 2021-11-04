# 그림
from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().rstrip().split())

graph = [list(stdin.readline().rstrip().split()) for _ in range(n)]
visited = [[0] * m for _ in range(n)] 

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    drawing = 0
    visited[x][y] = 1
    q = deque()
    q.append([x,y])

    while q:
        x, y = q.popleft()

        if graph[x][y] == '1':
            drawing += 1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '1' and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append([nx, ny])
    
    return drawing


cnt, result = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == '1' and visited[i][j] == 0:
            result = max(bfs(i, j), result)
            cnt += 1

print(cnt)
print(result)
            