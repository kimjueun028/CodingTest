def solution(s):
    answer = True
    l,r = 0,0
    for c in s:
        if c == '(':
            l += 1
        else:
            r += 1
        if l < r:
            answer = False
            break
    if l != r:
        answer = False
    return answer