from sys import stdin
import bisect
N = int(stdin.readline().strip())
card = sorted(list(map(int, stdin.readline().strip().split())))
M = int(stdin.readline().strip())
check = list(map(int,stdin.readline().strip().split()))

for c in check:
    i = bisect.bisect_left(card, c)
    if i < len(card) and card[i] == c:
        next = bisect.bisect_left(card,c+1)
        print(next-i, end=' ')
    else:
        print(0, end=' ')