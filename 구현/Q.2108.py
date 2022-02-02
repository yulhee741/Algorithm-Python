import sys
from collections import Counter

N = int(sys.stdin.readline())
li = []
for _ in range(N):
    li.append(int(sys.stdin.readline()))


# 산술평균
print(round(sum(li)/len(li)))

# 중앙값
li.sort()
print(li[(N-1)//2])

# 최빈값
if N == 1:
    print(li[0])
else:
    c = Counter(li).most_common(2)
    if c[0][1] == c[1][1]:
        print(c[1][0])
    else:
        print(c[0][0])

# 범위
print(li[-1] - li[0])