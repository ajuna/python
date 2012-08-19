print "Enter a string:"
s=input()

def verbing(s):
        if(len(s)>=3):
                if (s[-3:]=="ing"):
                        print s+"ly"
                else:
                        print s+"ing"
        else:
          print s

verbing(s)

