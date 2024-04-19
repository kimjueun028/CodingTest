def solution(arr, flag):
    X = []
    for i in range(len(flag)):
        num=arr[i]
        if flag[i]:
            for j in range(num):
                X.append(arr[i])
                X.append(arr[i])
        else:
            for k in range(num):
                X.pop()            
    return X