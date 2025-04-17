import sys
input = sys.stdin.readlines
user_input = input()

n = int(user_input[0])
arr = list(map(int, user_input[1].split()))
m = int(user_input[2])
targets = list(map(int, user_input[3].split()))

arr.sort()

for target in targets:
    start = 0
    end = n-1
    answer = 0
    while start <= end:
        mid = (start+end)//2
        
        if arr[mid] == target:
            answer = 1
            break
        elif arr[mid] > target:
            end = mid-1
        else:
            start = mid+1
    
    print(answer)