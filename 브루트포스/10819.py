# 차이를 최대로
from sys import stdin
from itertools import permutations

N = int(input())
nums = permutations(list(map(int, input().split())))

result = 0
for i in nums:
    sum = 0
    for j in range(N-1):
        sum += abs(i[j] - i[j+1])
    result = max(result, sum)

print(result)


















# from sys import stdin

# N = int(stdin.readline())
# nums = list(map(int, stdin.readline().split()))

# nums.sort()
# mid_toggle = 0
# if N % 2 != 0:
#     mid_num = nums.pop(int(N/2))
#     mid_toggle = 1

# result_s = []
# result_b = []
# count = len(nums)

# # 큰 수와 작은 수를 번갈아 정렬
# while count > 0 :
#     if count & 1:
#         result_s.append(nums.pop(0))
#     else:
#         result_b.append(nums.pop())
#     count-=1

# # 중간 수가 있다면 중간 수를 큰 수 리스트 맨 앞에 삽입
# if mid_toggle == 1:
#     result_b.insert(0,mid_num)
# else:
#     result_b.insert(0,result_b.pop(-1))
# ans = 0
# for i in range(int(N/2)):
#     if i == int(N/2)-1 and mid_toggle == 0:
#         ans += abs(result_b[i]-result_s[i])
#         break
#     else:
#         ans += abs(result_b[i]-result_s[i])
#         ans += abs(result_s[i]-result_b[i+1])
    
# print(ans)