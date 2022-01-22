# 도서관
from sys import stdin

n,m = map(int, stdin.readline().rstrip().split())
book = list(map(int, stdin.readline().rstrip().split()))

# 음수, 양수 나누기
left = []
right = []
for item in book:
    if item < 0:
        left.append(item)
    elif item > 0:
        right.append(item)

distance = []
left.sort()
for i in range(len(left)//m):
    distance.append(abs(left[m*i]))
if len(left) % m > 0:
    distance.append(abs(left[(len(left)//m)*m]))
    
right.sort(reverse = True)
for i in range(len(right)//m):
    distance.append(right[m*i]) 
if len(right) % m > 0:
    distance.append(right[(len(right)//m)*m])    
    
distance.sort()
result = distance.pop()
result += 2*sum(distance)
print(result)    