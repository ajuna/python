import sys
import re
def extract_names(filename):
  f=open(filename,'rU')
  text=f.readline()
  year_match=re.search(r'\d\d\d\d',text)
  print year_match.group()
  baby_names=re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>',text)
  names={}
  for name in baby_names:
	names.append(sorted(name))
	print names
  f.close()
  return extract_names

