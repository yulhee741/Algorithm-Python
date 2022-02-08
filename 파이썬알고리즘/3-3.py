# 뮤직비디오(결정알고리즘)
from sys import stdin

def count(capacity):
    cnt = 1
    sum_x = 0
    for x in music:
        if sum_x + x > capacity:
            cnt += 1
            sum_x = x
        else:
            sum_x += x
    return cnt

n, m = map(int, stdin.readline())
music = list(map(int, stdin.readline().split()))
maxx = max(music)
lt = 1
rt = sum(music)
res = 0
while lt <= rt:
    mid = (lt + rt) // 2
    if mid >= maxx and count(mid) <= m:
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(res)

