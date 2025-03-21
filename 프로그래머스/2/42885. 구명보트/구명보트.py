from collections import deque
def solution(people, limit):
    answer = 0
    '''
    큰 값부터 시작.
    가장 큰 값 80이 함께 탈 수 있는 사람 있는지 확인
    없다면 넘어가. 있다면 걔랑 탔을때 limit안넘을때까지 태움
    사람들 다 사라질때까지 더해야함. - while
    '''
    people.sort()
    people = deque(people)
    while people:
        current = people.pop()
        if people and people[0] <= (limit-current):
            current += people[0]
            people.popleft()
        answer += 1
    return answer
        