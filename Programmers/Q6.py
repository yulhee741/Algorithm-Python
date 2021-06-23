# 네이버 부스트캠프 자가진단 6번 문제입니다
# num array가 들어올 때 숫자들의 반복횟수 배열 형태로 리턴, 반복된 숫자가 없을 시 -1 리턴.

def count_dic(arr):
    ans_dic = {}
    for i in arr:
        if i not in ans_dic.keys():
            ans_dic[i] = 1
        else:
            ans_dic[i] += 1
    return ans_dic

def solution(arr):
    answer = []
    ans_dic = count_dic(arr)

    for j in ans_dic.values():
        if j != 1:
            answer.append(j)
        else:
            pass
    
    if len(answer) == 0:
        return -1
    else:
        return answer



arr = list(map(int, input("숫자 배열 입력: ").split(' ')))
print(arr)
print(solution(arr))