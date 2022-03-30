# 섬나라 아일랜드(BFS)
from sys import stdin
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
n = int(stdin.readline())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]
cnt = 0
q = deque()

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            board[i][j] = 0
            q.append((i, j))
            while q:
                tmp = q.popleft()
                for k in range(8):
                    x = tmp[0] + dx[k]
                    y = tmp[1] + dy[k]
                    if 0 <= x < n and 0 <= y < n and board[x][y] == 1:
                        board[x][y] = 0
                        q.append((x, y))
            cnt += 1
print(cnt)