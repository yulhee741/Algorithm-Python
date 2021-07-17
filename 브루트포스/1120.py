# 문자열
from sys import stdin

a, b = stdin.readline().split()
compare_ab = 0

# A를 B에 맞게 이동시켜가며 비교
# 빈칸은 B문자열에 맞게 넣는다고 생각하고 고려 안함.
for i in range(len(b)-len(a)+1):
    cnt = 0
    for j in range(len(a)):
        if a[j] == b[j+i]:
            cnt += 1
    if cnt > compare_ab:
        compare_ab = cnt

print(len(a)-compare_ab)

