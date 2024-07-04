def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if visited[i] == False:
            answer += 1
            # 연결 시작
            queue = [i]  # start // 방문예정목록
            while queue: 
                curr = queue.pop(0)
                visited[curr] = True
                for j in range(len(computers[curr])):
                    if computers[curr][j] == 1 and visited[j] == False:
                        queue.append(j)
                        visited[j] = True  # 방문처리
                        
    return answer