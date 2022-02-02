# 마법사 상어와 비바라기
from sys import stdin

n, m = map(int, stdin.readline().rstrip().split())
board = [list(map(int, stdin.readline().rstrip().split())) for _ in range(n)]
moves = [list(map(int, stdin.readline().rstrip().split())) for _ in range(m)]

clouds = [[n-2, 0], [n-2, 1], [n-1, 0], [n-1, 1]]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

for i in range(m):
    # 1
    move = moves[i]
    next_clouds = []

    for cloud in clouds:
        x, y = cloud[0], cloud[1]
        d, s = move[0] - 1, move[1]

        nx = (n + x + dx[d] * s) % n
        ny = (n + y + dy[d] * s) % n
        next_clouds.append([nx, ny])

    # 2
    visited = [[False] * n for _ in range(n)]
    for cloud in next_clouds:
        x, y = cloud[0], cloud[1]
        board[x][y] += 1
        visited[x][y] = True
    
    # 3
    clouds = []

    # 4
    cx = [-1, -1, 1, 1]
    cy = [-1, 1, -1, 1]
    for cloud in next_clouds:
        x, y = cloud[0], cloud[1]
        cnt = 0
        for i in range(4):
            nx = x + cx[i]
            ny = y + cy[i]

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] >= 1:
                cnt += 1
        
        board[x][y] += cnt
    
    # 5
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 2 and visited[i][j] == False:
                board[i][j] -= 2
                clouds.append([i,j])


print(sum(map(sum, board)))