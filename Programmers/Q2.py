def solution(param0):
    size_dict = {'BOOL': 1, 'SHORT': 2, 'FLOAT': 4, 'INT': 8, 'LONG': 16}
    size = [size_dict[t] for t in param0]
    result = []
    cur_str = ''

    for s in size:
        if len(cur_str) <= 8-s: # 공간 남음 -> 패딩 추가하고 이어 붙임
            cur_str += '.' * ((s-len(cur_str)) % s) + '#' * s
            if len(cur_str) == 8:
                result.append(cur_str)
                cur_str = ''
        else:               # 공간 없음 -> 끝까지 패딩으로 채우고 새로운 문자열 추가
            if len(cur_str):
                result.append(cur_str + '.' * (8-len(cur_str)))
                cur_str = ''
            if s >= 8:      # 8 or 16 -> cur_str은 공백으로 놔두고 result에 바로 추가
                for _ in range(s // 8):
                    result.append('########')
            else:           # cur_str에 추가
                cur_str = '#' * s

    if cur_str:             # cur_str이 비어있지 않으면 result에 추가
        result.append(cur_str + '.' * (8-len(cur_str)))

    return ','.join(result) if len(result) <= 16 else 'HALT'


param = ["INT", "INT", "BOOL", "SHORT", "LONG"]
print(solution(param))