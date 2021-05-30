# 오븐 시계
import sys

h, m = map(int, sys.stdin.readline().split())
cookingT = int(sys.stdin.readline())

totalM = m + cookingT # 요리시간과 현재 시간의 분을 합친 totalM

if totalM >= 60:    # 60분을 넘어설 경우 시간 + 1
    while totalM >= 60:
        h += 1
        totalM -= 60
        
if h >= 24:
    h -= 24

print(h, totalM)