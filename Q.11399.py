N=int(input())
list = list(map(int, input().split()))
# (1)대기시간이 짧은 사람 우선순위
list.sort()
result=0

# (2)첫번째인 사람은 사람수만큼 대기시간이 더해지고, 두번째인사람은 사람수-1만큼 대기시간이 더해짐...
for i in range(N):
    result += list[i]*(N-i)
print(result)