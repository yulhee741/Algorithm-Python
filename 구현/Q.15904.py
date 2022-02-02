string = input()
UCPC = []
cnt = 0
for i in string:
    if i == 'U' and cnt == 0:
        UCPC.append('U')
        cnt += 1
    elif i == 'C' and cnt == 1:
        UCPC.append('C')
        cnt += 1
    elif i == 'P' and cnt == 2:
        UCPC.append('P')
        cnt += 1
    elif i == 'C' and cnt == 3:
        UCPC.append('C')
        break

s = ''.join(UCPC)

if 'UCPC' in s:
    print("I love UCPC")
else:
    print("I hate UCPC")