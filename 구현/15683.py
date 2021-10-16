# 감시
import sys
N,M = map(int,sys.stdin.readline().split())
_map = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
tot = 0
cctv = []
U,D,L,R = [-1,0], [1,0], [0,-1], [0,1]
for i in range(N):
    for j in range(M):
        if _map[i][j] == 0: tot += 1
        elif 0 <_map[i][j] < 6 : cctv.append([i, j, _map[i][j]])
cctv_hist = [[] for _ in range(len(cctv))]
maxval = 0
def detect(index, d):
    for dir in d:
        hist = set()
        for yi, xi in dir:
            y, x = cctv[index][0], cctv[index][1]
            while 1:
                if 0 <= y + yi < N and 0 <= x + xi < M:
                    if _map[y + yi][x + xi] == 0:
                        hist.add((y + yi, x + xi))
                        y, x = y + yi, x + xi
                    elif 0 < _map[y + yi][x + xi] < 6: y, x = y + yi, x + xi
                    else: break
                else: break
        cctv_hist[index].append(hist)
for i in range(0, len(cctv)):
    if cctv[i][2] == 1:
        detect(i, [[U], [D], [L], [R]])
    elif cctv[i][2] == 2:
        detect(i, [[U, D], [L, R]])
    elif cctv[i][2] == 3:
        detect(i, [[R, U], [R, D], [L, D], [L, U]])
    elif cctv[i][2] == 4:
        detect(i,  [[U, R, D], [R, D,L], [D, L, U], [U, L, R]])
    elif cctv[i][2] == 5:
        detect(i, [[U, R, D, L]])
def DFS(depth,array):
    global maxval
    if depth == len(cctv) :
        cnt = len(array)
        if cnt > maxval : maxval = cnt
        return
    elif depth < len(cctv):
        for i in range(len(cctv_hist[depth])) :
            DFS(depth+1,array | cctv_hist[depth][i])
DFS(0, set())
print(tot - maxval)