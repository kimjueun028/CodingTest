import sys
input = sys.stdin.readlines
user_input = input()

A, B, C = list(i.strip() for i in user_input[:])

dot = str(int(A)*int(B)*int(C))

keys = [str(key) for key in range(0,10)]
my_dict = {key: 0 for key in keys}

for i in dot:
    my_dict[i] += 1

for value in my_dict.values():
    print(value)