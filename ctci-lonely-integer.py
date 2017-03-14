#!/bin/python
from functools import reduce
from operator import xor
import sys

def lonely_integer(a):
    return reduce(xor, a)    
    
n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
print lonely_integer(a)