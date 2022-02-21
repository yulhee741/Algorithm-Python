# 순열 추측하기
from sys import stdin

def DFS(l, sum_n):
    if l == n and sum_n == f:
        for x in p:
            print(x, end=' ')
        sys.exit(0)
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                p[l] = i
                DFS(l+1, sum_n+(p[l]*b[l]))
                ch[i] = 0

if __name__ == "__main__":
    n, f = map(int, stdin.readline().split())
    p = [0] * n # 순열
    b = [1] * n # 이항계수 저장
    ch = [0] * (n+1)
    for i in range(1, n):
        b[i] = b[i-1] * (n-i)//i
    DFS(0, 0)