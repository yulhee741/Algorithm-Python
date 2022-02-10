# 바닥 장식
from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
board = []
for _ in range(n):
    board.append(list(stdin.readline()))

cnt = 0
for i in range(n):
    pre = '\n'
    for j in range(m):
        if board[i][j] == '-':
            if board[i][j] != pre:
                cnt += 1
        pre = board[i][j]

for i in range(m):
    pre = '\n'
    for j in range(n):
        if board[j][i] == '|':
            if board[j][i] != pre:
                cnt += 1
        pre = board[j][i]

print(cnt)
    