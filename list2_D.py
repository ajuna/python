print "Enter a list of numbers:"
nums=input()

def remove_adjacent(nums):
	x=[]
	i=0
	n=len(nums)
	while(i<n):
		if(len(x)==0 or nums[i]!=x[-1]):
			x.append(nums[i])
		i=i+1
	print x
remove_adjacent(nums)
			
