# 컨베이어 벨트 위의 로봇
from sys import stdin

N, K = map(int, stdin.readline().split())
A_list = list(map(int, stdin.readline().split()))
robots = [0 for _ in range(N)]

ans = 1
while 1:
    # 1단계 회전
    A_list.insert(0, A_list.pop(-1))
    robots.insert(0, robots.pop(-1))
    robots[-1] = 0

    # 2단계 먼저 벨트에 올라간 로봇부터 한칸 이동
    for i in range(-2, -N-1, -1):
        if robots[i] == 1 and robots[i+1] == 0 and A_list[i+1-N] > 0:
            robots[i] = 0
            robots[i+1] = 1
            A_list[i+1-N] -= 1 
    robots[-1] = 0

    # 3단계 로봇 올림
    if robots[0] == 0 and A_list[0] > 0 :
        robots[0] = 1
        A_list[0] -= 1

    # 4단계 내구도 확인
    if A_list.count(0) >= K:
        break

    ans += 1

print(ans)
