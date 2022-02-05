# 회문 문자열 검사
from sys import stdin
n = int(stdin.readline())

for i in range(n):
    s = stdin.readline()
    s = s.upper() # 문자열 대문자화
    size = len(s)

    # for j in range(size//2):
    #     if s[j] != s[-1-j]:
    #         print("#%d NO" %(i+1))
    #         break
    # else:
    #     print("#%d YES" %(i+1))
    if s == s[::-1]:
        print("#%d YES" %(i+1))
    else:
        print("#%d No" %(i+1))
