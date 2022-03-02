# 동전 바꿔주기(DFS)
from sys import stdin

def DFS(l, coin):
    global cnt
    if l == k:
        if coin == T:
            cnt += 1
    else:
        for i in range(cn[l]+1):
            DFS(l+1, coin+(cv[l]*i))

if __name__=="__main__":
    T = int(stdin.readline())
    k = int(stdin.readline())
    cv = list()
    cn = list()
    for i in range(k):
        a, b = map(int, stdin.readline().split())
        cv.append(a)
        cn.append(b)
    cnt = 0
    DFS(0, 0)
    print(cnt)