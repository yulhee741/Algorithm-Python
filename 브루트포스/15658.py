from sys import stdin

N = int(stdin.readline().rstrip())
nums = list(map(int, stdin.readline().split()))
opers = list(map(int, stdin.readline().split()))

max_num = -1000000001
min_num = 1000000001

# + - * /
def cal(num, idx):
    global max_num, min_num
    if idx == N-1:
        max_num = max(max_num, num)
        min_num = min(min_num, num)
        return

    for i in range(4):
        if opers[i] != 0:
            opers[i] -= 1
            if i == 0:
                cal(num + nums[idx+1], idx+1)
            elif i == 1:
                cal(num - nums[idx+1], idx+1)
            elif i == 2:
                cal(num * nums[idx+1], idx+1)
            elif i == 3:
                cal(int(num/nums[idx+1]), idx+1)
            opers[i] += 1


cal(nums[0], 0)
print(max_num)
print(min_num)