import math

def solution(progresses, speeds):
    answer = []
    days = []   # queue
    for i in range(len(progresses)):
        x = (100-progresses[i]) / speeds[i]
        if int(x) == x:
            x = int(x)
        else:
            x = int(x)+1
        # x = math.ceil(x)
        days.append(x)
        
    while days:
        curr = days.pop(0)
        cnt = 1
        while days and curr >= days[0]:
            cnt += 1
            days.pop(0)
        answer.append(cnt)
    return answer