from sys import stdin
from collections import deque

def DFS(l, weight, t_sum):
    global weight
    if weight + (total - tsum) < result:
        return
    if weight > c:
        return
    if l == n:
        if weight > result:
            result = weight
    else:
        DFS(l+1, weight + a[l], tsum + a[l])
        DFS(l+1, weight, tsum + a[l])


if __name__=="__main__":
    c, n = map(int, stdin.readline().split())
    a = [0] * n
    result = -2147000000
    for i in range(n):
        a[i] = int(stdin.readline())
    total = sum(a)
    DFS(0, 0, 0)