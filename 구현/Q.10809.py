a_list = list( -1 for i in range(26))

string = input()
cnt = 0

for s in string:
    if a_list[ord(s) - 97] == -1:
        pass
    else:
        a_list[ord(s) - 97] = cnt
    cnt += 1

for i in range(len(a_list)) :
    print(a_list[i], end=' ')
