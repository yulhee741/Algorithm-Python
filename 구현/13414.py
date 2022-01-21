# 수강신청
from sys import stdin

k, l = map(int, stdin.readline().rstrip().split())
waiting = dict()

for i in range(l):
    number = stdin.readline().rstrip()

    if number not in waiting.keys():
        waiting[number] = i
    else:
        waiting.pop(number)
        waiting[number] = i

waiting_list =list(waiting.keys())
for num in waiting_list[:k]:
    print(num)
