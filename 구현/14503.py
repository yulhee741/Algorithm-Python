# 로봇 청소기
from sys import stdin
from collections import deque

def clean(x, y, d):
    global res
    if board[x][y] == 0:
        board[x][y] = 2
        res += 1
    for _ in range(4):
        i = (d + 3) % 4
        nx = x + dx[i]
        ny = y + dy[i]
        if board[nx][ny] == 0:
            clean(nx, ny, i)
            return
        d = i
    i = (d + 2) % 4
    nx = x + dx[i]
    ny = y + dy[i]
    if board[nx][ny] == 1:
        return
    clean(nx, ny, d)

n, m = map(int, stdin.readline().split())
r, c, d = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]
# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
res = 0
clean(r, c, d)
print(res)


