from collections import deque
def solution(priorities, location):
    answer = []
    queue = deque((k,v) for k,v in enumerate(priorities))
    while queue:
        process = queue.popleft()
        if queue and any(process[1] < another[1] for another in queue):
            queue.append(process)
        else:
            answer.append(process)
        
    for key, value in enumerate(answer):
        if value[0] == location:
            return key +1