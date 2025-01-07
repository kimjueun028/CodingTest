import sys
input = sys.stdin.readlines
user_input = input()
ls = list(int(i) for i in user_input[:])

result = []
for i in ls:
    new = i % 42
    if new not in result:
        result.append(new)
print(len(result))