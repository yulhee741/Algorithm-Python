n=int(input())
line=[]
for i in range(n):
  new_line = list(map(int, input().split()))  
  line.append(new_line)

for i in range(1,n):
  for j in range(len(line[i])):
    if j==0:
      line[i][j]=line[i][j]+line[i-1][j]
    elif j==len(line[i])-1: 
      line[i][j]=line[i][j]+line[i-1][j-1]
    else:
      line[i][j]=max(line[i-1][j-1],line[i-1][j])+line[i][j]
      
print(max(line[n-1]))