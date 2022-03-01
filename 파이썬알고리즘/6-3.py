# 양팔 저울(DFS)
from sys import stdin

def DFS(l, weight):
    global res
    if l == n:
        if 0 < weight <= s:
            res.add(weight)
    else:
        DFS(l+1, weight+G[l])
        DFS(l+1, weight-G[l])
        DFS(l+1, weight)

if __name__=="__main__":
    n = int(stdin.readline())
    G = list(map(int, stdin.readline().split()))
    s = sum(G)
    res = set()
    DFS(0, 0)
    print(s-len(res))