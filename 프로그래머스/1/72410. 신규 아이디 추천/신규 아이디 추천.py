def solution(new_id):
    # 1단계
    answer = new_id.lower()
    # 2단계
    filtered = []
    for c in answer:
        if c.isalpha() or c.isdigit() or c in ('-', '_', '.'):
            filtered.append(c)
    answer = "".join(filtered)
    # 3단계
    while '..' in answer:
        answer = answer.replace('..','.')
    # 4단계
    answer = answer.strip('.')
    # 5단계
    if not answer:
        answer = 'a'
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
    if answer[-1] == '.':
        answer = answer.rstrip('.')
    # 7단계
    while len(answer) < 3 :
        answer += answer[-1]
    return answer