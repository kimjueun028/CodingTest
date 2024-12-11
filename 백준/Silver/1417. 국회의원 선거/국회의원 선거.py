import sys
import heapq


input = sys.stdin.readlines
user_input = input()
N = int(user_input[0])
dasom = -int(user_input[1])
candidates = [-i for i in list(map(int, user_input[2:]))] # q

heapq.heapify(candidates)

def mesu(winner, others):
    if not others:
        return 0
    
    plus_vote = 0
    while winner >= min(others):
        candidate = heapq.heappop(others)
        heapq.heappush(others, int(candidate+1))
        winner -= 1
        plus_vote += 1
    return plus_vote

print(mesu(dasom, candidates))