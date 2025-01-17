import sys
input = sys.stdin.readlines
user_input = input()

N = int(user_input[0])
line = user_input[1].strip()
M = 1234567891
result = 0
for index, value in enumerate(line):
    result += (ord(value)-96)*31**index
print(result % M)
