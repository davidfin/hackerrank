from collections import Counter 
def ransom_note(magazine, ransom):
    return (Counter(ransom) - Counter(magazine)) == {}

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"
    