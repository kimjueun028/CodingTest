def solution(places):
    answers = []
    
    for place in places:
        key_P = []
        key_O = []
        for row, line in enumerate(place):            
            for col, table in enumerate(line):
                if table == 'P':
                    key_P.append((row, col))
                elif table == 'O':
                    key_O.append((row, col))
        
        answer = 1
        for i,j in key_P:
            if (i+1,j) in key_P or (i,j+1) in key_P:  # 거리:1
                answer-=1
                break
                
            if (i+1, j+1) in key_P:  # 거리:2 1번째
                if (i+1,j) in key_O or (i,j+1) in key_O:
                    answer-=1
                    break
            elif (i+1, j-1) in key_P:
                if (i,j-1) in key_O or (i+1,j) in key_O:
                    answer-=1
                    break
            elif (i+2,j) in key_P and (i+1,j) in key_O: # 거리:2 2번째
                answer-=1
                break
            elif (i,j+2) in key_P and (i,j+1) in key_O: # 거리:2 3번째
                answer-=1
                break
        
        answers.append(answer)

    return answers