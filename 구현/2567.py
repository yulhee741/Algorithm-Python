# 색종이 - 2
from sys import stdin

n = int(stdin.readline().rstrip())
board = [[0] * 101 for _ in range(101)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    x, y = map(int, stdin.readline().rstrip().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            board[i][j] = 1

result = 0

for i in range(1, 101):
    for j in range(1, 101):
        if board[i][j] == 1:
            cnt = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if board[nx][ny] == 1:
                    cnt += 1
            
            if cnt == 3:
                result += 1
            elif cnt == 2:
                result += 2

print(result)