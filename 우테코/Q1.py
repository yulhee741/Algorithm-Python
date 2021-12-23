def solution(time, plans):
    answer = ''
    total = 0
    for plan in plans:
        place, start, arrive = plan[0], plan[1], plan[2]
        
        if start[-2:] == "PM":  # 출발 시간이 오후일 때
            if int(start[:-2]) < 6:
                total += 6 - int(start[:-2])  # 써야할 휴가 시간 계산
        elif start[-2:] == "AM":  # 출발 시간이 오전일 때
            total += 18 - int(start[:-2])  # 써야할 휴가 시간 계산
                
        if arrive[-2:] == "PM":
            if int(arrive[:-2]) > 1: # 도착 시간이 오후 1시를 넘었을 때
                total += int(arrive[:-2]) - 1  # 써야할 휴가 시간 계산

        if total <= time:
            answer = place
            
    return answer

plans = [ ["홍콩", "11PM", "9AM"], ["엘에이", "3PM", "2PM"] ]
print(solution(3.5, plans))
