import sys
input = sys.stdin.readlines
A, B, C = list(map(int, input()))
print(A+B-C)
print(int(str(A)+str(B))-C)