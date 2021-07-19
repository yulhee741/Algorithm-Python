# 아기 상어 2
from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())


board = []
dq = deque()
# 그래프 생성
for n in range(N):
    board.append(list(map(int, stdin.readline().split())))
    for m in range(M):
        if board[n][m] == 1:
            dq.append([n,m])

dx = [-1, 0, 1, 1, 1, 0, -1, -1]
dy = [1, 1, 1, 0, -1, -1, -1, 0]

while dq:
        x, y = dq.popleft()
        for i in range(8):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 0:
                    dq.append((nx, ny))
                    board[nx][ny] = board[x][y] + 1


max_dis = max(map(max, board))
print(max_dis-1)