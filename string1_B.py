print "Enter a string"

s=input()
def both_ends(s):
        if len(s)>2:
                s=s[0:2]+s[-2:]
                print s

        else:
                print"Empty string"

both_ends(s)

