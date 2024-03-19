def solution(arr):
    answer = []
    if len(arr)>=2:
        k=arr.index(min(arr))
        del arr[k]
        answer = arr
    else:
        answer=[-1]
    return answer