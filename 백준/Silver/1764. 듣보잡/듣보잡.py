import sys
input = sys.stdin.readlines
user_input = input()
N, M = list(map(int,user_input[0].split()))

hear_set = set(i.strip() for i in user_input[1:N+1])
see_set = set(i.strip() for i in user_input[N+1:])

hear_see_set = hear_set.intersection(see_set)
hear_see_list = list(hear_see_set)
hear_see_list.sort()
print(len(hear_see_list))
for hear_see in hear_see_list:
    print(hear_see)