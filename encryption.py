#!/bin/python

import sys
from math import import ceil, sqrt

s = raw_input().strip(" ")
c = int(ceil(sqrt(len(s))))

transposed = map(lambda x: s[x::c], range(c))
print(' '.join(transposed))
