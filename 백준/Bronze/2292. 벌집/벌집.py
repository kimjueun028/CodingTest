import sys
input = sys.stdin.readline
N = int(input())

i = 0
temp = 1
while True:
    temp+=i*6
    if N <= temp:
        print(i+1)
        break
    i+=1