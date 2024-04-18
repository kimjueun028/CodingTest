def solution(arr, intervals):
    answer = []
    for i in range(len(intervals)):
        start=intervals[i][0]
        end=intervals[i][1]
        for j in range(start, end+1):
            answer.append(arr[j])
    return answer