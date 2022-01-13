# A -> B
from sys import stdin
a, b  = map(int, stdin.readline().split())
cnt = 1

while 1:
    if b == a:
        break
    if b < a or (b % 10 != 1 and b % 2 != 0):
        cnt = -1
        break
    elif b % 2 == 0:
        b //= 2
        cnt += 1
    elif b % 10 == 1:
        b //= 10
        cnt += 1

print(cnt)