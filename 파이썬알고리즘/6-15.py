# 토마토(BFS)
from sys import stdin
from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(m)]
q = deque()
dis = [[0]*n for _ in range(m)]
for i in range(m):
    for j in range(n):
        if board[i][j] == 1:
            q.append((i, j))
while q:
    tmp = q.popleft()
    for i in range(4):
        nx = tmp[0] + dx[i]
        ny = tmp[1] + dy[i]
        if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 0:
            board[nx][ny] = 1
            dis[nx][ny] = ds[tmp[0]][tmp[1]] + 1
            q.append((nx, ny))
flag = 1
for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            flag = 0
result = 0
if flag==1:
    for i in range(m):
        for j in range(n):
            if dis[i][j] > result:
                result = dis[i][j]
    print(result)
else:
    print(-1)
