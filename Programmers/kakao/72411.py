# 메뉴 리뉴얼

from itertools import combinations

def solution(orders, course):
    answer = []
    
    for i in course:
        order_dic = {}
        combination_list = []
        order_list = []
        
        for order in orders:
            combination_list += combinations(sorted(order), i)
        
        for combination in combination_list:
            s = ''.join(combination)
            order_list.append(s)
        
        for order in order_list:
            if order not in order_dic.keys():
                order_dic[order] = 1
            else:
                order_dic[order] += 1

        for k,v in order_dic.items():
            if max(order_dic.values()) == v and v > 1:
                answer.append(k)
        
    return sorted(answer)
    