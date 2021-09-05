# 오픈 채팅방 (10분)

def solution(record):
    answer = []
    record_dic = {}
    message_split = []
    
    for message in record:
        message_split = message.split()
        if message_split[0] == "Enter":
            record_dic[message_split[1]] = message_split[2]
        elif message_split[0] == "Change":
            record_dic[message_split[1]] = message_split[2]
    
    for message in record:
        message_split = message.split()
        if message_split[0] == "Enter":
            answer.append(record_dic[message_split[1]] + "님이 들어왔습니다.")
        elif message_split[0] == "Leave":
            answer.append(record_dic[message_split[1]] + "님이 나갔습니다.")
 
    return answer