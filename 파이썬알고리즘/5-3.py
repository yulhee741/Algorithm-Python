# 부분집합 구하기(DFS)
from sys import stdin

def DFS(v):
    if v == n+1:
        for i in range(1, n+1):
            if ch[i] == 1:
                print(i, end=' ')
        print()
    else:
        ch[v] = 1
        DFS(v+1)
        ch[v] = 0
        DFS(v+1)


if __name__=="__main__":
    n = int(stdin.readline())
    ch = [0] * (n+1)
    DFS(1)