# 폴짝폴짝
from sys import stdin
from collections import deque

n = int(stdin.readline().rstrip())
steps = list(map(int, stdin.readline().rstrip().split()))
a, b = map(int, stdin.readline().rstrip().split())

def bfs(a, b, steps, n):
    q = deque()
    q.append(a-1)
    check = [-1] * n
    check[a-1] = 0

    while q:
        node = q.popleft()
        for i in range(node, n, steps[node]):
            if check[i] == -1:
                q.append(i)
                check[i] = check[node] + 1
                if i == b-1:
                    return check[i]
        for i in range(node, -1, -steps[node]):
            if check[i] == -1:
                q.append(i)
                check[i] = check[node] + 1
                if i == b-1:
                    return check[i]
    return -1

print(bfs(a,b,steps,n))