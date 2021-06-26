# 프린터 큐
import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    numbD, pos = map(int, sys.stdin.readline().split()) # 문서의 갯수, 원하는 문서 위치 입력
    importance = list(map(int, sys.stdin.readline().split())) # 문서의 중요도 입력

    check = [0 for i in range(numbD)]
    check[pos] = 1 # 0 리스트 중 알기 원하는 위치에 1 입력

    dq = deque(importance) # 덱 선언
    cnt = 0 # 출력 횟수 카운트
    while 1:
        if dq[0] == max(dq):    # 덱의 첫번째가 가장 중요도가 크다면
            if check[0] == 1:   # 원하는 위치인지 판별 후 카운트 세기
                cnt += 1
                break
            else:
                dq.popleft()    # 원하는 위치가 아닐경우 pop, cnt + 1
                check.pop(0)
                cnt += 1
        else:
            dq.append(dq.popleft()) # 가장 중요도가 크지 않다면 덱의 맨 뒤에 append
            check.append(check.pop(0))
    print(cnt)
        