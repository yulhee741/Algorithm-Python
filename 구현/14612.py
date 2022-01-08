# 김식당
from sys import stdin

n, m = map(int, stdin.readline().rstrip().split())
post = {}

for i in range(n):
    command = list(stdin.readline().rstrip().split())

    if command[0] == 'order':
        post[int(command[1])] = int(command[2])
    elif command[0] == 'sort':
        post = dict(sorted(post.items(), key=lambda x : (x[1], x[0])))
    elif command[0] == 'complete':
        del post[int(command[1])]

    if len(post) == 0:
        print("sleep")
        continue

    for table in post.keys():
        print(table, end=' ')
    print("")


