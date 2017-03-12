# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input()) 
names = []
phone = []
for line in range(0,n): 
	entry = raw_input().split(" ")
	names.append(entry[0])
	phone.append(entry[1])

book = dict(zip(names, phone)) 

while True:
	try:
		line = raw_input()
		print line + "=" + book[line]
	except KeyError: 
		print "Not found"
	except EOFError:
		break

