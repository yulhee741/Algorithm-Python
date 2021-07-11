#행렬의 곱셈

def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        result = []
        for j in range(len(arr2[0])):
            sum_num = 0
            for k in range(len(arr1[0])):
                sum_num += arr1[i][k] * arr2[k][j]
            
            result.append(sum_num)
        answer.append(result)
    return answer