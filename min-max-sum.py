#!/bin/python

import sys


a,b,c,d,e = raw_input().strip().split(' ')
l = [int(a),int(b),int(c),int(d),int(e)]
total_sum = sum(l)

minimum = total_sum
maximum = 1

for i in range(0, 5): 
	local_sum = total_sum - l[i] 
	if local_sum < minimum: 
		minimum = local_sum     
	if local_sum > maximum: 
		maximum = local_sum

print str(minimum) + " " + str(maximum)
