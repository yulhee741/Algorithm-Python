# 퇴사
import sys

N = int(sys.stdin.readline().rstrip())

table = []
for i in range(N):
    t, p = map(int, sys.stdin.readline().split())
    table.append((t,p))

dp = [0 for _ in range(N+1)]

#맨 마지막 일부터 돈 벌 수 있는 경우 체크
for i in range(N-1, -1, -1):
    tmp = i + table[i][0]
    #마지막 인덱스일 경우, 상담 일이 하루면 dp에 p를 넣어줌
    if i == N-1:
        if table[i][0] == 1:
            dp[i] = table[i][1]
    elif tmp == N:
        dp[i] = max(table[i][1], dp[i+1])
    elif tmp < N:
        dp[i] = max(table[i][1] + dp[tmp], dp[i+1])
    else:
        dp[i] = dp[i+1]

print(dp[0])