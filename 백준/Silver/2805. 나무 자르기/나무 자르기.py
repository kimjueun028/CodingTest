import sys
input = sys.stdin.readlines
user_input = input()

n, m = list(map(int, user_input[0].split()))
trees = list(map(int, user_input[1].split()))

start = 0
end = max(trees)
height = 0

while start <= end:
    total = 0
    mid = (start+end)//2
    for tree in trees:
        if tree > mid:
            total += (tree-mid)
    
    if total >= m:
        start = mid+1
        height = mid
    else:
        end = mid-1

print(height)