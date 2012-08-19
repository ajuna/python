 
print "Enter two words"
a=input()
b=input()


def mix_up(a,b):

 print"%s %s"%(b[:2]+a[2:],a[:2]+b[2:])


mix_up(a,b)
