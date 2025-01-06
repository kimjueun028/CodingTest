import sys
input = sys.stdin.readlines
user_input = input()

T = int(user_input[0])
arr = [list(map(int, i.split())) for i in user_input[1:]]

for H, W, N in arr:
    floor = N%H
    if not floor:
        floor = H
        ho = N//H
    else:
        ho = (N//H) +1
    
    if not ho:
        ho = 1

    if ho < 10:
        ho = '0' + str(ho)
    else:
        ho = str(ho)
    
    print(str(floor)+ho)