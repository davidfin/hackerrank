
n = input()
ar = map(int, raw_input().strip().split(' '))
count = [ar.count(i) for i in xrange(max(ar)+1)]

printout = []
for i in xrange(len(count)):
    printout += [i] * count[i]
        
print ' '.join(map(str, printout))
