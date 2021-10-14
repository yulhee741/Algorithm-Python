# 후보 추천하기
import sys import stdin.readline
from collections import deque

N , M = int(stdin.readline()) , int(stdin.readline())
pick_num = list(map(int, stdin.readline().split()))
photo , dic = [], dict()
for data in pick_num:
    if data in photo:
        dic[data] +=1
    elif len(photo) < N :
        photo.append(data)
        dic[data] = 1
    else:
        pick = photo[0]
        for k in photo:
            if dic[pick] > dic[k]:
                pick = k
        photo.remove(pick)
        photo.append(data)
        dic[data] = 1
print(*sorted(photo))