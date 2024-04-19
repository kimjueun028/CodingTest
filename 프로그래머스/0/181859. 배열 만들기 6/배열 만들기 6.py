def solution(arr):
    stk = []
    i=0
    arr_len=len(arr)
    while i<arr_len:
        if not stk or stk[-1]!= arr[i]:
            stk.append(arr[i])
            i+=1
        else:
            stk.pop()
            i+=1
    if not stk:
        stk.append(-1)
    return stk 