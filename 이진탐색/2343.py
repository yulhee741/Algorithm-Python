# 기타 레슨
from sys import stdin

n, m = map(int, stdin.readline().split())
lessons = list(map(int, stdin.readline().split()))

left = max(lessons)
right = sum(lessons)
result = sum(lessons)

while left <= right:
    mid = (left+right)//2
    cnt = 0
    tmp = 0
    
    for i in range(n):
        if tmp + lessons[i] > mid:
            cnt += 1
            tmp = 0
        tmp += lessons[i]
    if tmp > 0:
        cnt += 1 

    if cnt > m:
        left = mid + 1
    else:
        right = mid - 1
        if result > mid:
            result = mid

print(result)