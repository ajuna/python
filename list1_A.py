print "Enter a list:"
list=input()

def match_ends(list):
	i=0
	count=0
	l=len(list)
	while (i<l):
		if (len(list[i])>1 and list[i][0]==list[i][-1]):
			count=count+1
		i=i+1
	print count

match_ends(list)


		

