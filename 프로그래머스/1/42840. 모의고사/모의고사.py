def solution(answers):
    scores = []
    patterns = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    
    for pattern in patterns:
        len_answers, len_pattern = len(answers), len(pattern)
        student = pattern*(len_answers//len_pattern) + pattern[:(len_answers%len_pattern)]
        cnt = 0
        for num in range(len_answers):
            if answers[num] == student[num]:
                cnt += 1
        scores.append(cnt)
        
    best_score = max(scores)  
    return [index+1 for index, score in enumerate(scores) if score == best_score]