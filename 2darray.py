#!/bin/python

import sys


arr = []
for arr_i in xrange(6):
	arr_temp = map(int,raw_input().strip().split(' '))
	arr.append(arr_temp)

m = -100 

for i in range(0,4): 
	for j in range(0,4): 
		top = arr[i][j:j+3]
		middle = [arr[i+1][j+1]]
		bottom = arr[i+2][j:j+3]
		hour_glass = top + middle + bottom 
		sum_hour_glass = sum(hour_glass) 

		if sum_hour_glass > m:
			m = sum_hour_glass


print m

