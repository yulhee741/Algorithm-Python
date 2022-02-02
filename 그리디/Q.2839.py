kg = int(input())
result = 0
flag = 0
while kg != 0:
    if kg < 0:
        result = -1
        break
    if kg % 5 == 0:
        result += kg // 5
        kg = kg % 5
    else :
        kg -= 3
        result += 1

print(result) 
