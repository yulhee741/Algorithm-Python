from sys import stdin

n=int(stdin.readline())
command=[]
for _ in range(n):
    command.append(stdin.readline().split())

now=''
skip=int(command[-1][2])+1

for c in command[::-1]:
    if skip<=int(c[2]):
        continue
    if c[0]=='undo':
        skip=int(c[2])-int(c[1])
    else:
        now=c[1]+now
print(now)
        