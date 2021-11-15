# 배열 돌리기 1
from sys import stdin

n, m, r = map(int, stdin.readline().rstrip().split())
board = [list(map(int, stdin.readline().rstrip().split())) for _ in range(n)]

for _ in range(r):
    for i in range(min(n, m) // 2):
        x, y = i, i
        tmp = board[x][y]

        for j in range(i + 1, n - i):  # 왼쪽
            x = j
            pre = board[x][y]
            board[x][y] = tmp
            tmp = pre

        for j in range(i + 1, m - i):  # 아래쪽
            y = j
            pre = board[x][y]
            board[x][y] = tmp
            tmp = pre

        for j in range(i + 1, n - i):  # 오른쪽
            x = n - j - 1
            pre = board[x][y]
            board[x][y] = tmp
            tmp = pre

        for j in range(i + 1, m - i):  # 위쪽
            y = m - j - 1
            pre = board[x][y]
            board[x][y] = tmp
            tmp = pre

for i in range(n):
    for j in range(m):
        print(board[i][j], end=' ')
    print()

