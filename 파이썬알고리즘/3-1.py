# 이분검색
from sys import stdin

n, m = map(int, stdin.readline().split())
a = list(map(int, stdin.readline().split()))
a.sort()
lt = 0
rt = n-1
while lt <= rt:
    mid = (lt+rt)//2
    if a[mid] == m:
        print(mid+1)
        break
    elif a[mid] > m:
        rt = mid-1
    else:
        lt = mid+1

