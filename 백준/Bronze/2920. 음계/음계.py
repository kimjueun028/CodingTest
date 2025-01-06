import sys
input = sys.stdin.readline

melody = list(map(int, input().split()))

ascen = [i for i in range(1,9)]
descen = [i for i in range(8,0,-1)]

if melody == ascen:
    print('ascending')
elif melody == descen:
    print('descending')
else:
    print('mixed')