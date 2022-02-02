n, m = map(int, input().split())
j = int(input())
point = []
distance = 0
left = 1
right = m
for i in range(j):
    p = int(input())
    point.append(p)

for i in range(len(point)):
    tmp = 0
    if point[i] > right: #박스보다 오른쪽
        tmp += abs(point[i] - right)
        distance += tmp
        right +=  tmp
        left += tmp
    elif point[i] < left:
        tmp += abs(point[i] - left)
        distance += tmp
        right -= tmp
        left -= tmp
    elif left < point[i] < right:
        pass

print(distance)
