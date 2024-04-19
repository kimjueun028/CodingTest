def solution(l, r):
    answer = []
    for i in range(l,r+1):
        ms = str(i)
        idx = 0
        for j in ms:
            if j in ['0','5']:
                idx += 1
                pass
            else:
                break
        if idx == len(ms):
            answer.append(i)
    if len(answer)==0:
        answer.append(-1)
    return answer