#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
	a_temp = map(int,raw_input().strip().split(' '))
	a.append(a_temp)

s2 = 0
s1 = 0

for i in range(0,n):
    	s2 = s2 + a[i][n-i-1]
	s1 = s1 + a[i][i]

s = s1 -s2

if (s < 0): 
	print s*(-1)
else:
	print s 
