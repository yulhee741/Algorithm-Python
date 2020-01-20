n, m = map(int, input().split())
nums=[int(i) for i in input().split()]
list=[]

# 카드의 합이 m을 넘지 않을 때에 list[]에 넣고, 그 중 가장 큰 값 출력

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            sum = nums[i]+nums[j]+nums[k]
            if sum <= m:
                list.append(sum)
            

print(max(list))
