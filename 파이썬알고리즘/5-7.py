# 동전 교환
from sys import stdin

def DFS(l, coin):
    global res
    if l > res:
        return
    if coin > m:
        return
    if coin == m:
        if l < res:
            res = l
    else:
        for i in range(n):
            DFS(l+1, coin + a[i])

if __name__=="__main__":
    n = int(stdin.readline())
    a = list(map(int, stdin.readline()))
    m = int(stdin.readline())
    res = 2147000000
    a.sort(reverse=True)
    DFS(0, 0)
    print(res)