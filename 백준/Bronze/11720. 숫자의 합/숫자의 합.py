import sys
input = sys.stdin.readlines
user_input = input()

N = int(user_input[0])
ls = user_input[1].strip()

result = 0
for i in ls:
    result += int(i)
print(result)