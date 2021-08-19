# 숫자판 점프
from sys import stdin

graph = [list(stdin.readline().split())for _ in range(5)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


result = []
def dfs(x, y, num):
    if len(num) == 6:
        result.append(num)
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 5 and 0 <= ny < 5:
                dfs(nx, ny, num + graph[nx][ny])  

for x in range(5):
    for y in range(5):
        num = graph[x][y]
        dfs(x, y, num)

print(len(set(result)))