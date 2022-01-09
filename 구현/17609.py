# 회문
from sys import stdin

T = int(stdin.readline().rstrip())

def is_palindrome(s):
    if s == s[::-1]:
        return 0
    else:
        return 1

# def is_palindrome(ss):
#     s = list(str(ss))

#     if list(reversed(ss)) == s:
#         return 0
#     else:
#         return 1

for _ in range(T):
    ss = stdin.readline().rstrip()
    check = False

    # 회문 확인
    if is_palindrome(ss) == 0:
        print(0)
        continue
    else:
        # 유사 회문 확인
        for i in range(len(ss)):
            s = ss[:i] + ss[i+1:]
            if is_palindrome(s) == 0:
                print(1)
                check = True
                break
        if check == False:
            print(2)
    