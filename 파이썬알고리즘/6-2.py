# 휴가(DFS)
from sys import stdin

def DFS(l, score):
    global res
    if l == n+1:
        if score > res:
            res = score
    else:
        if l+T[l] <= n+1:
            DFS(l+T[l], score+P[l])
        DFS(l+1, score)

if __name__=="__main__":
    n = int(stdin.readline())
    T = list()
    P = list()
    for i in range(n):
        a, b = map(int, stdin.readline().split())
        T.append(a)
        P.append(b)
    res = -2147000000
    T.insert(0, 0)
    P.insert(0, 0)
    DFS(1, 0)