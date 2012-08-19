print 'Enter a list of strings:'
list=input()

def front_x(list):
	i=0
	l=len(list)
	list_x=[]
	list_nx=[]	
	while (i<l):
		if (list[i].startswith('x')):
			list_x.append(list[i])
		else:
			list_nx.append(list[i])
			
		i=i+1
				
	print list_x
	print list_nx
	print sorted(list_x)+sorted(list_nx)

front_x(list)
