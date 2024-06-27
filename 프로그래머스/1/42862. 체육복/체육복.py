def solution(n, lost, reserve):
    k = []
    answer = 0
    lost.sort()
    reserve.sort()
    #arr = [i for i in range(1,n+1)]
    #for i in range(1,n+1):
    #    arr.append(i)
    for j in range(1, n+1):
        if j not in lost and j not in reserve:
            k.append(j)
        elif j in lost and j in reserve:
            k.append(j)
            lost.remove(j)
            reserve.remove(j)
    for m in reserve:
        if (m-1) in lost and (m+1) in lost:
            k.append(m)
            k.append(m-1)
            lost.remove(m-1)
        elif (m-1) in lost and (m+1) not in lost:
            k.append(m)
            k.append(m-1)
            lost.remove(m-1)
        elif (m-1) not in lost and (m+1) in lost:
            k.append(m)
            k.append(m+1)
            lost.remove(m+1)
        elif (m-1) not in lost and (m+1) not in lost:
            k.append(m)
    answer = len(k)
    return answer