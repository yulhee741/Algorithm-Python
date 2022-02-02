s= input()
c_num = len(s)

for i in range(len(s)-1) :
    if s[i] + s[i+1] == 'c=':
        c_num -= 1
    elif s[i] + s[i+1] == 'c-':
        c_num -= 1
    elif s[i] + s[i+1] == 'd-':
        c_num -= 1
    elif s[i] + s[i+1] == 'lj':
        c_num -= 1
    elif s[i] + s[i+1] == 'nj':
        c_num -= 1
    elif s[i] + s[i+1] == 's=':
        c_num -= 1


for j in range(len(s)-1) :
    if s[j] + s[j+1] =='z=':
        if s[j-1] == 'd':
            c_num -= 2
        else:
            c_num -= 1


print(c_num)