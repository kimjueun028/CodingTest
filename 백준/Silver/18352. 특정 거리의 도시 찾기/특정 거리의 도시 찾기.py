import sys
import heapq

input = sys.stdin.readlines
user_input = input()
N, M, K, X = list(map(int,user_input[0].split()))
arrs = [list(map(int, i.split())) for i in user_input[1:]]

graph = [[] for _ in range(N)]
for start_node, end_node in arrs:
    graph[start_node-1].append(end_node-1)

visited = [False] * N

distances = [float("inf")] * N

q = []
distances[X-1] = 0
heapq.heappush(q, (distances[X-1], X-1))
visited[X-1] = True
result = []
while q:
    dist, now_index = heapq.heappop(q)
    visited[now_index] = True
    if graph[now_index]:
        for next_index in graph[now_index]:
            if visited[next_index] == False and (dist+1) < distances[next_index]:
                distances[next_index] = (dist+1)
                heapq.heappush(q, (distances[next_index], next_index))
    if dist == K:
        result.append(now_index+1)

if result:
    result.sort()
    while result:
        print(result.pop(0))
else:
    print(-1)