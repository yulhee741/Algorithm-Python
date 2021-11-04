# 양
from sys import stdin
from collections import deque

r, c = map(int, stdin.readline().rstrip().split())
graph = [list(stdin.readline().rstrip()) for i in range(r)]

visited = [[0] * c for i in range(r)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    sheep, wolf = 0, 0
    q = deque()
    q.append([x,y])

    while q:
        x, y = q.popleft()
        if graph[x][y] == 'o':
            sheep += 1
        elif graph[x][y] == 'v':
            wolf += 1
        graph[x][y] = '.'
        visited[x][y] = 1
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != '#' and visited[nx][ny] != 1:
                visited[nx][ny] = 1
                q.append([nx, ny])

    if wolf >= sheep:
        sheep = 0
    else:
        wolf = 0
    return sheep, wolf


sheep_cnt, wolf_cnt = 0, 0
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'o' or graph[i][j] == 'v':
            sheep, wolf = bfs(i,j)
            sheep_cnt += sheep
            wolf_cnt += wolf

print(sheep_cnt, wolf_cnt)
