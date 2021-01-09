num = int(input())

list = []
for i in range(num) :
    list.append(input())

cnt = 0
#입력받은 수만큼 for문 돌기
for i in range(num) :
    #빈 리스트 생성
    str = []
    #리스트 i번째 원소의 글자 개수가 1일 경우 무조건 카운트 +1
    if len(list[i]) == 1:
        str.append(list[i][0])
        cnt += 1
    else:
        #리스트 글자 하나씩 탐색
        for j in range(len(list[i])):
            #마지막 글자가 str리스트에 없다면 카운트 +1 마지막번째 글자에서 다음 글자를 비교할 수 없기때문에 if문사용
            if j == len(list[i])-1:
                if not list[i][-1] in str:
                    cnt += 1
            else:
                #현재 글자와 다음 글자가 다를 경우에만 str리스트에 append
                if not list[i][j] == list[i][j+1]:
                    if list[i][j] in str:
                        break
                    else:
                        str.append(list[i][j])

print(cnt)