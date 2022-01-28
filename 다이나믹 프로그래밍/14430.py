# 자원 캐기
from sys import stdin

n, m = map(int, stdin.readline().rstrip().split())
board = [list(map(int, stdin.readline().rstrip().split(' '))) for _ in range(n)]
source = [[0] * m for _ in range(n)]

source[0][0] = board[0][0]

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            continue
        elif i > 0 and j == 0:
            source[i][j] = source[i-1][j]
        elif i == 0 and j > 0:
            source[i][j] = source[i][j-1]
        else:
            source[i][j] = max(source[i-1][j], source[i][j-1])
        if board[i][j] == 1:
            source[i][j] += 1

print(source[n-1][m-1])
