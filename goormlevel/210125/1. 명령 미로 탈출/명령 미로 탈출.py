# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
raw_input = sys.stdin.readlines
user_input = raw_input()
N, K = list(map(int,user_input[0].strip().split()))
order = user_input[1].strip()
M = [row.strip().split() for row in user_input[2:]]

for i in range(N):
		for j in range(N):
			if M[i][j] == '1':
				row, col = i, j
				break

directions = {'U':(-1,0), 'D':(1,0), 'L':(0,-1), 'R':(0,1)}
cnt = 0
sign = 'FAIL'

for c in order:
	d_row, d_col = directions[c]
	if 0<=row+d_row<N and 0<=col+d_col<N:  # index 시에는 항상 범위 확인 -1이면 안됨~
		curr = M[row + d_row][col + d_col]
		if curr == '2':
			cnt += 1
			sign = 'SUCCESS'
			break
		elif curr == '0' or curr == '1':
			row, col = row+d_row, col+d_col
			cnt += 1	

if sign == 'SUCCESS':
	print(sign +' '+ str(cnt))
else:
	print(sign)