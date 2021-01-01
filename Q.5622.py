list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

dial = input()
time = 0
#dial 글자 하나씩 비교
for i in dial :
    for j in range(len(list)):
        #만약 i 글자가 list에 있을 경우 시간 +3
        if i in list[j]:
            time += (j+3)

print(time)
    