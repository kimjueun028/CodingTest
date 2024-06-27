def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            queue = [i]
            while queue: #추가하고 방문한 애는 안감
                visit = queue.pop(0)
                if not visited[visit]:
                    for j in range(n):
                        if j!=visit and computers[visit][j] == 1:
                            queue.append(j)
                    visited[visit] = True
            answer += 1
            
    return answer