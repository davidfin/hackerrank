#!/bin/python

import sys

n = int(raw_input().strip())

def decimalToBinary(n):
	if n==0: 
		return ''
	else:
	return decimalToBinary(n/2) + str(n%2)

def getConsecutive(n): 
	m = 1
	count = 0
	for c in n:
	if c == '1': 
		count = count + 1
	else: 
		count = 0
	if count > m: 
		m = count
	return m

binary = decimalToBinary(n)
print getConsecutive(binary)

