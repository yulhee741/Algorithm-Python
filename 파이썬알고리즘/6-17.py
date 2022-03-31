# 피자배달거리(DFS)
from sys import stdin

def DFS(L, s):
    global res
    if L==m:
        sum_dis = 0
        for j in range(len(hs)):
            x1 = hs[j][0]
            y1 = hs[j][1]
            dis = 2147000000
            for x in cb:
                x2 = pz[x][0]
                y2 = pz[x][1]
                dis = min(dis, abs(x1-x2) + abs(y1-y2))
            sum_dis += dis
        if sum_dis < res:
            res = sum_dis
    else:
        for i in range(s, len(pz)):
            cb[L] = i
            DFS(L+1, i+1)


if __name__=="__main__":
    n, m = map(int, stdin.readline().split())
    board = [list(map(int, stdin.readline().split())) for _ in range(n)]
    hs = []
    pz = []
    cb = [0]*m
    res = 2147000000
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                hs.append((i, j))
            elif board[i][j] == 2:
                pz.append((i, j))
    DFS(0, 0)