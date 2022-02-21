# 조합구하기(DFS)
from sys import stdin

def DFS(l, s):
    global cnt
    if l == m:
        for j in range(l):
            print(res[j], end=' ')
        cnt += 1
        print()
    else: 
        for i in range(s, n + 1):
            res[l] = i
            DFS(l+1, i+1)


if __name__=="__main__":
    n, m = map(int, stdin.readline().split())
    res = [0] * (n+1)
    cnt = 0
    DFS(0, 1)
    print(cnt)
