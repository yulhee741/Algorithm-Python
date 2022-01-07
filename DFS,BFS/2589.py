# 보물섬
from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().rstrip().split())
graph = [list(stdin.readline().rstrip()) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
q = deque()

def bfs(y, x):
    q.append([y,x])
    ch = [[0] * m for _ in range(n)]
    ch[y][x] = 1
    dis = 0

    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if graph[ny][nx] == 'L' and ch[ny][nx] == 0:
                    ch[ny][nx] = ch[y][x] + 1
                    dis = max(dis, ch[ny][nx])
                    q.append([ny,nx])
    return dis - 1

cnt = 0
for y in range(n):
    for x in range(m):
        if graph[y][x] == 'L':
            cnt = max(cnt, bfs(y,x))

print(cnt)