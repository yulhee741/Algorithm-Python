import sys
n = int(sys.stdin.readline())
pair = int(sys.stdin.readline())

matrix = [[0]*(n+1) for i in range(n+1)]
visited = [False for i in range(n+1)]
cnt = -1 #1번 컴퓨터는 제외

for j in range(pair):
    x, y = map(int, sys.stdin.readline().split())
    matrix[x][y] = matrix[y][x] = 1

def dfs(v):
    global cnt
    visited[v] = True
    cnt += 1
    for i in range(1, n+1):
        if visited[i] == False and matrix[v][i] == 1:
            dfs(i)

dfs(1)

print(cnt)