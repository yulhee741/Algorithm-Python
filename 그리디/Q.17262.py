import sys
N = int(sys.stdin.readline())
s_list = [0 for i in range(N)]
for i in range(N):
    s_list[i] = list(map(int, sys.stdin.readline().split()))

come = sorted(s_list, key=lambda x:x[0]) #등교시간 빠른 순서
out = sorted(s_list, key=lambda x:x[1]) #하교시간 빠른 순서
result =  come[-1][0] - out[0][1]

if result <= 0:
    print(0)
else:
    print(result)