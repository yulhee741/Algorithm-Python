# 카드 놓기
from sys import stdin
from itertools import permutations

N = int(stdin.readline().rstrip())
K = int(stdin.readline().rstrip())

card_list = []
for _ in range(N):
    card_list.append(stdin.readline().rstrip())


result = []
for x in permutations(card_list, K):
    result.append(''.join(x))

result = list(set(result))
print(len(result))
