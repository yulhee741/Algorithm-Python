# 랜선자르기(결정알고리즘)
from sys import stdin

def count(length):
    cnt = 0
    for x in Line:
        cnt += (x//length)
    return cnt

k, n = map(int, stdin.readline().split())
Line = []
res = 0
largest = 0
for i in range(k):
    tmp = int(stdin.readline())
    Line.append(tmp)
    largest = max(largest, tmp)

lt = 1
rt = largest
while lt <= rt:
    mid = (lt + rt)//2
    if count(mid) >= n:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(res)