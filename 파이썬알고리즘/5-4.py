# 합이 같은 부분집합(DFS)
from sys import stdin

def DFS(l, sum_n):
    if sum_n > total//2: # 시간 복잡도 줄이기
        return
    if l == n:
        if sum_n == (total - sum_n):
            print("YES")
            sys.exit(0)
    else:
        DFS(l+1, sum_n+a[l])
        DFS(l+1, sum_n)

if __name__=="__main__":
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    total = sum(a)
    DFS(0, 0)
    print("NO")
