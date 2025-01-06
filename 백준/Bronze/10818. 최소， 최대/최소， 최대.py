import sys
input = sys.stdin.readlines
user_input = input()

N = int(user_input[0])
ls = list(map(int, user_input[1].split()))

print(min(ls), max(ls))