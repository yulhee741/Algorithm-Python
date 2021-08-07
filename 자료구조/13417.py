# 카드 문자열
from sys import stdin
from collections import deque

T = int(stdin.readline().rstrip())

for _ in range(T):
    N = int(stdin.readline().rstrip())
    cards = stdin.readline().split()
    q = deque()
    q.append(cards[0])
    for i in range(1,len(cards)):
        if cards[i] <= q[0]:
            q.appendleft(cards[i])
        else:
            q.append(cards[i])
    print("".join(q))