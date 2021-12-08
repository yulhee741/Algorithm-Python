# 후보 추천하기
from sys import stdin

n = int(stdin.readline())
cnt = int(stdin.readline())
pick_num = list(map(int, stdin.readline().split()))

photo = []
photo_dic = {}
for pick in pick_num:
    if len(photo) < n:
        if pick not in photo:
            photo_dic[pick] = 1
            photo.append(pick)
        else:
            photo_dic[pick] += 1
    else:
        if pick in photo:
            photo_dic[pick] += 1
        else:
            # key_min = min(photo_dic, key=photo_dic.get)
            idx = photo.index(key_min)
            photo[idx] = pick
            del(photo_dic[key_min])
            photo_dic[pick] = 1

photo.sort()
print(*photo)