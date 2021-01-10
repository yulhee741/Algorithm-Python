import itertools

n, m = map(int, input().split())
nums=[int(i) for i in input().split()]
arr=[]

# 카드의 합이 m을 넘지 않을 때에 list[]에 넣고, 그 중 가장 큰 값 출력
nCr = list(itertools.combinations(nums,3))
for i in nCr:
    if sum(i) <= m:
        arr.append(int(sum(i)))
           
print(max(arr))
