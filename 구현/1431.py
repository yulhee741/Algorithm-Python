# 시리얼 번호
from sys import stdin

n = int(stdin.readline().rstrip())

guitar = list(stdin.readline().rstrip() for _ in range(n))

def sum_serial(s):
    result = 0
    for i in s:
        if i.isdigit():
            result += int(i)
    return result

guitar.sort(key = lambda x: (len(x), sum_serial(x), x))

for s in guitar:
    print(s)