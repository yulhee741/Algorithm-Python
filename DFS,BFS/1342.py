# 행운의 무자열
from sys import stdin

def dfs(depth, s):
    global n, result, char_set, check_char
    if depth == n:
        result += 1
        return

    for char in char_set:
        idx = ord(char) - ord('a')
        if check_char[idx] == 0:
            continue
        if s and s[-1] == char:
            continue
        check_char[idx] -= 1
        dfs(depth + 1, s + char)
        check_char[idx] += 1


ss = stdin.readline().rstrip()
check_char = [0] * 26
n = len(ss)
result = 0
char_set = set()

for s in ss:
    idx = ord(s) - ord('a')
    check_char[idx] = check_char[idx] + 1
    char_set.add(s)

dfs(0, '')
print(result)