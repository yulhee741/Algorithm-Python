# 최대점수 구하기(DFS)
from sys import stdin

def DFS(l, score, time):
    global res
    if time > m:
        return
    if l == n:
        if score > res:
            res = score
    else:
        DFS(l+1, score + pv[l], time+pt[l])
        DFS(l+1, score, time)

if __name__=="__main__":
    n, m = map(int, stdin.readline().split())
    pv = list()
    pt = list()
    for i in range(n):
        a, b = map(int, stdin.readline().split())
        pv.append(a)
        pt.append(b)
    res = -2147000000
    DFS(0, 0, 0)
    print(res)