# 폴리오미노
from sys import stdin

board = stdin.readline().rstrip()

splited_points = board.split(".")
result = ''

for point in splited_points:
    if len(point) % 2 == 1:
        print("-1")
        exit()
    else:
        if len(point) > 2:
            n, r = divmod(len(point), 4)
            result += 'AAAA' * n
            if r != 0:
                result += 'BB'
        elif len(point) == 2:
            result += 'BB'
        result += '.'

print(result[:-1])