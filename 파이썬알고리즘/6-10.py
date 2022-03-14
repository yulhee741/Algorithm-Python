# 미로탐색(DFS)
from sys import stdin
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def DFS(x, y):
    global cnt
    if x==6 and y==6:
        cnt += 1
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= 6 and 0 <= ny <= 6 and board[nx][ny] == 0:
                board[nx][ny] = 1
                DFS(nx, ny)
                board[nx][ny] = 0

if __name__=="__main__":
    board = [list(map(int, stdin.readline().split())) for _ in range(7)]
    cnt = 0
    board[0][0] = 1
    DFS(0, 0)
    print(cnt)