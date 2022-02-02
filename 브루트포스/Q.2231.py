num = int(input())
generator = 0

for i in range(1, num+1):
    c = i
    #숫자 분해 후 각 자리수마다 더한 뒤에 num과 같을 경우 break
    string = str(c)
    for j in string:
        c += int(j)
    if c == num:
        generator = i
        break

print(generator)
     
