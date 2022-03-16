# 단지 번호 붙이기(DFS)
from sys import stdin

def DFS(x, y):
    global cnt
    cnt += 1
    board[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1:
            DFS(nx, ny)


if __name__=="__main__":
    n = int(stdin.readline())
    board = [list(map(int, stdin.readline())) for _ in range(n)]
    res = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                cnt = 0
                DFS(i, j)
                res.append(cnt)
    print(len(res))
    res.sort()
    for x in res:
        print(x)