import sys
input = sys.stdin.readlines
user_input = input()

S = user_input[0].strip()
i = int(user_input[1])

print(S[i-1])