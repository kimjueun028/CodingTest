import sys
input = sys.stdin.readlines
ls = list(map(int, input()))
max_index, max_value = 0, 0

for index, value in enumerate(ls):
    if value > max_value:
        max_value = value
        max_index = index
print(max_value)
print(max_index+1)