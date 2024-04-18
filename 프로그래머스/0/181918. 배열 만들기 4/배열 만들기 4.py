def solution(arr):
    stk = []
    i = 0
    while i <len(arr):
        if len(stk) == 0:
            stk.append(arr[i])
            i+=1
        else:
            while arr[i]<=stk[-1]:
                stk.pop()
                if len(stk)==0:
                    break
            stk.append(arr[i])
            i+=1
            
    return stk
