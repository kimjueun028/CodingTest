def solution(arr1, arr2):
    # answer = [[0   for jdx in range(len(arr1[idx]))]   for idx in range(len(arr1))]
    answer = arr1.copy()
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            answer 
            answer[i][j]=arr1[i][j] + arr2[i][j]
    
    # answer = []
    # for i in range(len(arr1)):
    #     temp = []
    #     for j in range(len(arr1[i])):
    #         temp.append(arr1[i][j] + arr2[i][j])
    #     answer.append(temp)
    return answer
