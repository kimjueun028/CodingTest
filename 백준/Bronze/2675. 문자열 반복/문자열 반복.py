import sys
input = sys.stdin.readlines
user_input = input()
T = int(user_input[0])
arr = [list(i.split()) for i in user_input[1:]]

for num, noun in arr:
    result = ''
    for one in noun:
        result += one*int(num)
    print(result)