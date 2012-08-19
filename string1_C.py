print "Enter a string:"
s=input()


def fix_start(s):
 s=s[0]+s[1:].replace(s[0],'*')
 print s
fix_start(s)

