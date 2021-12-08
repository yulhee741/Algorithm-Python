import sys
from collections import deque
sys.setrecursionlimit(10000)  # 런타임 방지
# 유기농 배추
def dfs(x, y):
    visited[x][y] = True
    for i in range(4):
        nx, ny = dx[i]+x, dy[i]+y
        if (0 <= nx < N) and (0 <= ny < M):
            if matrix[nx][ny] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                dfs(nx, ny)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

T = int(sys.stdin.readline())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().rstrip().split())

    matrix = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    count = 0

    for _ in range(K):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        matrix[y][x] = 1
    print(matrix)
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1 and visited[i][j] == False:
                dfs(i, j)
                count += 1

    print(count)