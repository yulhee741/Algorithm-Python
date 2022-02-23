# ZOAC
from sys import stdin

ss = list(stdin.readline().rstrip())
visited = [False] * len(ss)
def DFS(left, right):
    if left == right:
        return
    min_s = min(ss[left:right])
    min_idx = ss[left:right].index(min_s) + left
    visited[min_idx] = True

    for i in range(len(ss)):
        if visited[i]:
            print(ss[i], end='')
    print()
    DFS(min_idx+1, right)
    DFS(left, min_idx)

DFS(0, len(ss))