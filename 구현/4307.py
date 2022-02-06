# 개미
from sys import stdin
t = int(stdin.readline())

for _ in range(t):
    l, ants = map(int, stdin.readline().rstrip().split())
    smallest = 0
    largest = 0
    for ant in range(ants):
        point = int(stdin.readline().rstrip())
        smallest = max(smallest, min(point, l-point))
        largest = max(largest, max(point, l-point))

    print(smallest, largest)
    

