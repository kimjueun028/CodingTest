import sys
input = sys.stdin.readlines
user_input = input()

T = int(user_input[0])
arr = [list(map(int, i.split())) for i in user_input[1:]]

for testcase in arr:
    A, B = testcase
    print(A+B)