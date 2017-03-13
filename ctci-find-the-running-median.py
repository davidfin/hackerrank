#!/bin/python

import sys    
from heapq import heappush, heappop

class MedianHeap():
    def __init__(self):
        self.left = []   # max heap
        self.right = []  # min heap
        
    def push(self, value):
        if not self.left or value < -self.left[0]:  
            heappush(self.left, -value)  
        else:
            heappush(self.right, value)
        
        self.rebalance()
        
    def rebalance(self): 
        bigger = self.left if (len(self.left) > len(self.right)) else self.right
        smaller = self.left if len(self.left) < len(self.right) else self.right
        if len(bigger) - len(smaller) > 1:  
            moved = -1 * heappop(bigger)
            heappush(smaller, moved)
            
    def median(self):
        bigger = self.left if len(self.left) > len(self.right) else self.right
        smaller = self.left if len(self.left) < len(self.right) else self.right

        if bigger is smaller:
            return (self.right[0] - self.left[0]) / 2.0 
        else:
            maxi = -1.0 if bigger is self.left else 1.0
            return maxi * bigger[0]
            
n = int(raw_input().strip())

a_i = 0

heap = MedianHeap()

for a_i in xrange(n):
    a_t = int(raw_input().strip())

    heap.push(a_t)
    print heap.median() 