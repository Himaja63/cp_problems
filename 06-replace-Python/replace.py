# Without using the builtin method s.replace(), 
# write its equivalent. Specifically, write the function 
# replace(s1, s2, s3) that returns a string equal to 
# s1.replace(s2, s3), but again without calling s.replace().

import itertools
def fun_replace(s1, s2, s3):
	res = ""
	l1 = list(s1)
	l2 = list(s2)
	l3 = list(s3)
	if(s2 in s1):
		for i in range(len(l1)):
			if (l1[i] == l2[0]):
				if(l1[i:i+len(l2)] == l2):
					x = i
					y = 0
					if(len(s3) <= len(s2)):
						while(y < len(l2)):
							if(y < len(l3)):
								l1[x] = l3[y]
							else:
								l1[x] = "-"
							x = x + 1
							y = y + 1
					else:
						while(y < len(s2)-1):
							l1[x] = l3[y]
							x = x+1
							y = y+1
						l1[x] = l3[y:]

		list2d = l1
		merged = list(itertools.chain(*list2d))
		s = "".join(merged)
		for i in s:
			if(i != "-"):
				res = res+i
		return res
	else:
		return s1

