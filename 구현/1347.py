# 미로 만들기
from sys import stdin

n = int(stdin.readline().rstrip())
directions = stdin.readline().rstrip()

points = [(0, 0)]
dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1] # 북 동 남 서
status = 2 

for way in directions:
    if way == 'R':
        status = (status + 1) % 4
    elif way == 'L':
        status = (status - 1) % 4
    else:
        x = points[-1][1] + dx[status]
        y = points[-1][0] + dy[status]
        points.append((y, x))

x_sort = sorted(points, key=lambda x: x[1])
y_sort = sorted(points, key=lambda x: x[0])
x_min, x_max = x_sort[0][1], x_sort[-1][1]
y_min, y_max = y_sort[0][0], y_sort[-1][0]

maze = [list('#' for y in range(x_min, x_max + 1)) for x in range(y_min, y_max + 1)]

# 최소값 음수일경우 양수로 바꾸기
for i in range(len(points)):
    points[i] = (points[i][0] - y_min, points[i][1] - x_min)

for y, x in points:
    maze[y][x] = '.'

for row in maze:
    print(''.join(row))
