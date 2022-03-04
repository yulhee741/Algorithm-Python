from sys import stdin
from collections import deque

n = int(stdin.readline())
s_card = list(int(stdin.readline().rstrip()) for _ in range(n))
card_list = list(i for i in range(1, 2*n + 1))
g_card = [item for item in card_list if item not in s_card]
s_card.sort()
s = deque(s_card)
g = deque(g_card)

s_cnt, g_cnt = 0, 0
turn = True
card = 0

def check(card, q):
    nums = list(q)
    for num in nums:
        if num > card:
            return num
    return None

while s and g:
    if turn == True:
        if card == 0:
            card = s.popleft()
        else:
            tmp = check(card, s)
            if tmp == None:
                card = 0
            else:
                card = tmp
                s.remove(tmp)
    else:
        if card == 0:
            card = g.popleft()
        else:
            tmp = check(card, g)
            if tmp == None:
                card = 0
            else:
                card = tmp
                g.remove(tmp)
    turn = ~turn

print(len(g))
print(len(s))