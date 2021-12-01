# 경비원
from sys import stdin

w, h = map(int, stdin.readline().split())
store = int(stdin.readline())

points = []
for _ in range(store):
    way, distance  = map(int, stdin.readline().split())
    points.append((way, distance))
x, y = map(int, stdin.readline().split())

# 1: 북, 2: 남, 3: 서, 4: 동
def get_distance(x, y, way, dis):
    if x == 1:
        if way == 1:
            return abs(y - dis)
        if way == 2:
            return min((y + dis + h), ((2 * w) + h - y - dis))
        if way == 3:
            return  y + dis
        if way == 4:
            return  w - y + dis
    if x == 2:
        if way == 1:
            return min((y + dis + h), ((2 * w) + h - y - dis))
        if way == 2:
            return abs(y - dis)
        if way == 3:
            return h - dis + y
        if way == 4:
            return w - y + h - dis
    if x == 3:
        if way == 1:
            return y + dis
        if way == 2:
            return h - y + dis
        if way == 3:
            return abs(y - dis)
        if way == 4:
            return min((y + dis + h), ((2 * w) + h - y - dis))
    if x == 4:
        if way == 1:
            return w - dis + y
        if way == 2:
            return h - y + w - dis
        if way == 3:
            return min((y + dis + h), ((2 * w) + h - y - dis))
        if way == 4:
            return abs(y - dis)



result = 0
for way, distance in points:
    result += get_distance(x, y, way, distance)

print(result)