# 인접행렬
from sys import stdin
n, m = map(int, stdin.readline().split())
g = [[0] * (n+1) for_ in range(n+1)]

for i in range(m):
    a, b, c = map(int, stdin.readline().split())
    g[a][b] = c

for i in range(1, n+1):
    for j in range(1, n+1):
        print(g[i][j], end=' ')
    print()