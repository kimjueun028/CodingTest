def solution(s):
    answer = []
    s = s.split(" ")
    for noun in s:
        for index,value in enumerate(noun):
            if index % 2:
                answer.append(value.lower())
            else:
                answer.append(value.upper())
        answer.append(" ")
    return "".join(answer)[:-1]