# 욱제는 결정장애야!!
from sys import stdin

n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
sticker = []
max_n = 0
cnt = 0

for num in nums:
    if num in sticker:
        cnt -= 1
    elif num not in sticker:
        sticker.append(num)
        cnt += 1
    max_n = max(max_n, cnt)

print(max_n)