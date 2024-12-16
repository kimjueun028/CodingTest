import sys
input = sys.stdin.readlines
user_input = input()
N = int(user_input[0])

parti = list(i.strip() for i in user_input[1:N+1])
done = list(i.strip() for i in user_input[N+1:])

all_dict = {}
for one in parti:
    if one in all_dict:
        all_dict[one] += 1
    else:
        all_dict[one] = 1

for one in done:
    all_dict[one] -= 1

for name, num in all_dict.items():
    if num:
        print(name)
        break