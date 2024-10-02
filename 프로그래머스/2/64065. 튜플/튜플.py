def solution(s):
    answer = []
    s = s[2:-2]
    k = s.split("},{")
    ls = [i.split(',') for i in k]
    for i in sorted(ls, key=lambda x: len(x)):
        for j in i:
            if int(j) not in answer:
                answer.append(int(j))
    return answer