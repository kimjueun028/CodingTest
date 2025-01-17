import sys
input = sys.stdin.readlines
user_input = input()

N = int(user_input[0])
line = user_input[1].strip()

temp = []
for i in line:
    temp.append(ord(i)-96)

result=0
for index, value in enumerate(temp):
    result += value * 31**(index)
print(result)