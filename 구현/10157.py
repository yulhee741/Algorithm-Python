# 자리배정
from sys import stdin

c, r = map(int, stdin.readline().split())
k = int(stdin.readline())

board = [[0] * c for _ in range(r)]
x, y = r-1, 0
board[x][y] = 1
i = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while True:
    if k > c*r:
        print(0)
        break
    if board[x][y] == k:
        print(y+1, r-x)
        break
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < r and 0 <= ny < c and board[nx][ny] == 0:
        board[nx][ny] = board[x][y] + 1
        x, y = nx, ny
    else:
        i = (i + 1) % 4
