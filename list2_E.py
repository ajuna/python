print "Enter two lists:"
list1=input()
list2=input()

def linear_merge(list1,list2):
	list=[]
	list=list1+list2
	list.sort()
	print list
linear_merge(list1,list2)

