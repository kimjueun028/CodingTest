from collections import deque

def solution(begin, target, words):
    if not target in words:
        return 0
    
    queue = deque([(begin,0)])
    ls = [[w for w in word] for word in words]
    visited = [False for _ in range(len(words))]
    answer = 0
    
    while queue:
        current, answer = queue.popleft()

        if current == target:
            return answer
        
        idx = 0
        for l in ls:
            if not visited[idx]:
                cnt = 0
                for i in range(len(l)):
                    if l[i] != current[i]:
                        cnt += 1
                if cnt == 1:
                    answer += 1
                    queue.append((''.join(l), answer))
                    visited[idx] = True
            idx += 1
    return 

'''
최단경로를 구하는 거니까 bfs
hit hot 될라면 가운데 한칸만 이동해야하고
hot dot 될라면 첫번째 한칸만 이동해야하고
dot dog 될라면 마지막 한칸만 이동해야하고

하나만 다른 녀석을 골라야하고
visited하지 않았던 애를 골라야하고

hit -> hot 1
hot -> dot2 lot 2
dot -> lot3 dog 3
lot -> dog log 4
dog -> log cog 4
log -> cog

'''