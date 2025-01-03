import sys
input = sys.stdin.readlines
user_input = input()

N, X = list(map(int, user_input[0].split()))
ls = list(map(int, user_input[1].split()))

result = []
for i in ls:
    if i < X:
        print(i, end=' ')