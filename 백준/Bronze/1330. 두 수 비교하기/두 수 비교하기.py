import sys
input = sys.stdin.readline
user_input = input()
A, B = list(map(int, user_input.split()))

if A < B:
    print("<")
elif A > B:
    print(">")
else:
    print("==")