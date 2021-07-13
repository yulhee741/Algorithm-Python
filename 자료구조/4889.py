# 안정적인 문자열
from sys import stdin

idx = 1

while True:
    brackets = stdin.readline().rstrip()
    replace_bk = brackets.replace('{}','')
    while True:
        if '{}' in replace_bk:
            replace_bk = replace_bk.replace('{}','')
        else:
            break
        
    if '-' in replace_bk:
        break

    cnt = 0
    for i in range(len(replace_bk)):
        if i % 2 == 0 and replace_bk[i] !='{':
            cnt+=1
        if i % 2 == 1 and replace_bk[i] !='}':
            cnt+=1
      
    print(str(idx) + "." , cnt)
    idx += 1 
