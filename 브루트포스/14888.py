# 연산자 끼워넣기
from sys import stdin
from itertools import permutations

n = int(stdin.readline())
nums = list(map(int,stdin.readline().split()))
ops = list(map(int,stdin.readline().split()))

# 입력받은 명령어 저장
op=''
for idx,val in enumerate(ops):
    op += str(idx) * val


op = list(map(int,op))
result=[]

for now_op in set(permutations(op,len(op))):
    res = nums[0]
    for idx in range(n-1):
        if now_op[idx] == 0:
            res += nums[idx + 1]
        elif now_op[idx] == 1:
            res -= nums[idx + 1]
        elif now_op[idx] == 2:
            res *= nums[idx + 1]
        elif now_op[idx] == 3:
            res = int(res/nums[idx + 1])
            
    result.append(res)

print(max(result))
print(min(result))