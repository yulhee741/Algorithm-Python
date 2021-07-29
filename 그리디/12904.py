# A와 B
from sys import stdin

S = stdin.readline().rstrip()
T = stdin.readline().rstrip()

# B를 제거하고 문자열을 뒤집는다
# A를 제거한다
t = T
ans = 0
while t:
    if t == S:
        ans = 1
        break
    elif t[-1] == 'A':
        t = t[:-1]
    elif t[-1] == 'B':
        t = t[:-1]
        t = t[::-1]
    
print(ans)