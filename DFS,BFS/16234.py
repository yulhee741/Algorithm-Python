# 인구이동
from sys import stdin
from collections import deque

n, l, r = map(int, stdin.readline().rstrip().split())
graph = [list(map(int, stdin.readline().rstrip().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    move_q = deque()
    q.append([x,y])
    visited[x][y] = 1
    people, cnt = 0, 0

    while q:
        x, y = q.popleft()
        move_q.append([x,y])
        people += graph[x][y]
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                    visited[nx][ny] = cnt
                    q.append([nx,ny])

    while move_q:
        x, y = move_q.popleft()
        graph[x][y] = people // cnt

    if cnt == 1:
        return 0
    return 1


result = 0
while 1:
    q = deque()
    visited = [[0] * n for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                cnt += bfs(i,j)

    if not cnt:
        break
    result += 1
print(result)