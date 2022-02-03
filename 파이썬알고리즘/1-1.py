# K번째 약수
from sys import stdin

n, k = map(int, stdin.readline().split())

cnt = 0
for i in range(1, n+1):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break

else:
    print(-1)