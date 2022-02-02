N=int(input())
meeting=[]

for i in range(N):
  meeting.append(list(map(int,input().split())))

meeting.sort(key=lambda x:x[0])
#끝나는 시간순서로 정렬
meeting.sort(key=lambda x:x[1])

#회의 첫번째 start,end 넣기
start,end=meeting[0]
count = 1
for i in meeting[1:]:
    k,v=i
    if end <= k:
        end = v
        start = k
        count+=1

print(count)