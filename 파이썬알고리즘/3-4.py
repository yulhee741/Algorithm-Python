# 마구간 정하기(결정알고리즘)
from sys import stdin

def count(dis):
    cnt = 1
    ep = line[0]
    for i in range(1, n):
        if line[i] - ep >= dis:
            cnt += 1
            ep = line[i]
    return cnt

n, c = map(int, stdin.readline().split())
line = []
for _ in range(n):
    tmp = int(stdin.readline())
    line.append(tmp)
line.sort()
lt = 1
rt = line[n-1]
while lt <= rt:
    mid = (lt+rt)//2
    if  count(mid) >= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(res)