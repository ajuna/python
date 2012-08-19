print "Enter a sentence(with 'not...bad') :"
s=input()

def not_bad(s):
        n=s.find("not")
        b=s.find("bad")
        if(n<b):
                print s.replace(s[n:b+3],"good")
        else:
                print s


not_bad(s)

