# 1이 될 때까지
# 나의 풀이
from sys import stdin

n, k = map(int, stdin.readline().split())

result = 0
while 1:
    if n == 1:
        break
    if n % k == 0:
        n = n // k
        result += 1
    else:
        n -= 1
        result += 1

print(result)

