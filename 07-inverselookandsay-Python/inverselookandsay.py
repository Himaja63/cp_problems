# Write the function inverseLookAndSay(a) that does the inverse of the previous problem, so that, in general:
#       inverseLookAndSay(lookAndSay(a)) == a
# Or, in particular:
# inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10]
# inverseLookAndSay([]) == []
# inverseLookAndSay([(3,1)]) == [1,1,1]
# inverseLookAndSay([(1,-1),(1,2),(1,7)]) == [-1,2,7]
# inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10]
# inverseLookAndSay([(2,3),(1,8),(4,3)]) == [3,3,8,3,3,3,3])

def inverselookandsay(a):
	# Your code goes here
	l = []
	if (len(a) == 0 ):
		return l
	else:
		for i in range(len(a)):
			x = a[i]
			if(len(x)>0):
			    for j in range(x[0]):
			        l.append(x[1])
			else:
			    l = []
		return l

