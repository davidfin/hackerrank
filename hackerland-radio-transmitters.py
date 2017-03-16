#!/bin/python

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
x = map(int,raw_input().strip().split(' '))

numTransmitters = 0
i = 0
a = sorted(x)

while i < n:
    numTransmitters = numTransmitters + 1
        
    loc = a[i] + k
    
    while(i < n and a[i] <= loc):
        i = i + 1
        
    i = i - 1   # place transmitter

    loc = a[i] + k
    while(i < n and a[i] <= loc):
        i = i + 1

print numTransmitters   