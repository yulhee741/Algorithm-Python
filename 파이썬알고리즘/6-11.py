# 등산 경로(DFS)
from sys import stdin

def DFS(x, y):
    global cnt
    if x == ex and y == ey:
        cnt += 1
    else:
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and ch[nx][ny] == 0 and board[nx][ny] > board[x][y]:
                ch[nx][ny] = 1
                DFS(nx, ny)
                ch[nx][ny] = 0
            


if __name__=="__main__":
    n = int(stdin.readline())
    board = [[0]*n for _ in range(n)]
    ch = [[0]*n for _ in range(n)]
    max = -2147000000
    min = 2147000000
    for i in range(n):
        tmp = list(map(int, stdin.readline().split()))
        for j in range(n):
            if tmp[j] < min:
                min = tmp[j]
                sx = i
                sy = j
            if tmp[j] > max:
                max = tmp[j]
                ex = i
                ey = j
            board[i][j] = tmp[j]
    ch[sx][sy] = 1
    cnt = 0
    DFS(sx, sy)
    print(cnt)