def solution(arr):
    answer = []
    for key, value in enumerate(arr):
        if key == 0:
            answer.append(value)
        elif arr[key-1] != value:
            answer.append(value)
    return answer