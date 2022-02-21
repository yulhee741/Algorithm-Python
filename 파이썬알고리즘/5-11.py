# 수들의 조합(DFS)
from sys import stdin

def DFS(l, s, sum_n):
    global cnt
    if l == k:
        if sum_n % m == 0:
            cnt += 1
    else:
        for i in range(s, n):
            DFS(l+1, i+1 , sum_n + a[i])

if __name__=="__main__":
    n, k = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))
    m = int(stdin.readline())
    cnt = 0
    DFS(0, 0, 0)
    print(cnt)