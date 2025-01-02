import sys
input = sys.stdin.readline
ls = list(map(int, input().split()))

num = 0
for i in range(5):
    num += ls[i]**2

print(num%10)