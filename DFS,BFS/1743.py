# 음식물 피하기
from sys import stdin
from collections import deque

# 세로, 가로, 음식물 쓰레기의 개수
N, M, K = map(int, stdin.readline().split())
graph = [[0]*M for _ in range(N)]
visited = [[0]*M for _ in range(N)]

for k in range(K):
    x, y = map(int, stdin.readline().split())
    graph[x-1][y-1] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q = deque()
def bfs():
    q.append((n,m))
    food_waste = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    food_waste += 1
    return food_waste


result = 0
for n in range(N):
    for m in range(M):
        if graph[n][m] == 1 and visited[n][m] == 0:
            visited[n][m] = 1
            cnt = bfs()
            if result < cnt:
                result = cnt

print(result)