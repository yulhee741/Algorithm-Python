# 주유소
from sys import stdin
N = int(stdin.readline().rstrip())
dis = list(map(int, stdin.readline().split()))
prices = list(map(int, stdin.readline().split()))

result = 0
min_price = prices[0]

for i in range(len(dis)):
    if prices[i] < min_price:
        min_price = prices[i]
    result += min_price * dis[i]

print(result)



