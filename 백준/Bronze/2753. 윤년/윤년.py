import sys
input = sys.stdin.readline
N = int(input())

if not N % 4:
    if N % 100:
        print(1)
    else:
        if N % 400:
            print(0)
        else:
            print(1)
else:
    print(0)