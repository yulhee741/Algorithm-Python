# 안테나
from sys import stdin

n = int(stdin.readline().rstrip())
house = list(map(int, stdin.readline().rstrip().split()))

house.sort()
print(house[(n-1)//2])

