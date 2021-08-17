# 숫자 정사각형
from sys import stdin

n, m = map(int, stdin.readline().split())
board = []
for _ in range(n):
    board.append(stdin.readline())

side = min(n,m)

result = []
for i in range(n):
    for j in range(m):
        for k in range(side):
            if i+k < n and j+k < m and board[i][j] == board[i][j+k] == board[i+k][j] == board[i+k][j+k]:
                result.append(k+1)


print(max(result)**2)