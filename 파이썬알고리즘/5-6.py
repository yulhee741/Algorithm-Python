# 중복 순열 구하기(DFS)
from sys import stdin

def DFS(l):
    global cnt
    if l == m:
        for j in range(m):
            print(res[j], end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n+1):
            res[l] = i
            DFS(l+1)

if __name__=="__main__":
    n, m = map(int, stdin.readline().split())
    res = [0] * m
    cnt = 0
    DFS(0)
    print(cnt)