# 내리막 길
from sys import stdin
from collections import deque

m, n = map(int, stdin.readline().rstrip().split())
graph = [list(map(int, stdin.readline().rstrip().split())) for _ in range(m)]

result = [[-1] * n for _ in range(m)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def calc(result, table, m, n, x, y):
    if x == m - 1 and y == n - 1:
        result[x][y] = 1
        return
    if result[x][y] != -1:
        return
    result[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if graph[x][y] > graph[nx][ny]:
                calc(result, graph, m, n, nx, ny)
                result[x][y] += result[nx][ny]

calc(result, graph, m, n, 0, 0)
print(result[0][0])