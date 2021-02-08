import sys
import heapq

N = int(input())
list = []

for i in range(N):
    num = int(sys.stdin.readline())
    if num > 0:
        heapq.heappush(list, num)
    elif num == 0:
        if len(list) == 0:
            print(0)
        else:
            print(heapq.heappop(list))