# 오목
from sys import stdin

n = 19
board = [list(map(int, stdin.readline().rstrip().split())) for _ in range(n)]

dx = [1, 1, 0, -1]
dy = [0, 1, 1, 1]

for x in range(n):
    for y in range(n):
        if board[x][y]:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                cnt = 1

                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue

                while 0 <= nx < n and 0 <= ny < n and board[x][y] == board[nx][ny]:
                    cnt += 1

                    if cnt == 5:
                        if 0 <= nx + dx[i] < n and 0 <= ny + dy[i] < n and board[nx][ny] == board[nx + dx[i]][ny + dy[i]]:
                            break
                        if 0 <= x - dx[i] < n and 0 <= y - dy[i] < n and board[x][y] == board[x - dx[i]][y - dy[i]]:
                            break
                        print(board[x][y])
                        print(x+1, y+1)
                        exit()

                    nx += dx[i]
                    ny += dy[i]

print(0)
