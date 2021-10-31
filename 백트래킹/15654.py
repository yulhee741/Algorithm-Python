# N과 M(5)
from sys import stdin

n, m = map(int, stdin.readline().split())
nums = list(stdin.readline().split())
nums.sort()
checked = [False] * n
result = [0] * m

def go(cnt):
    if cnt == m:
        print(*result)
        return 

    for i in range(len(nums)):
        if checked[i] == True:
            continue
        checked[i] = True
        result[cnt] = nums[i]            
        go(cnt + 1)
        checked[i] = False


go(0)
