# Here we will rewrite the previous function to be destructive. This version must not just call the nondestructive 
# version from above and then clear and replace the values in the original list. Instead, you must traverse the list 
# once and make the changes to the list as you go. With that in mind, write the destructive function shortenLongRuns(
# L, k) that takes a list L and a positive integer k, and destructively modifies L by removing any values in L that 
# would otherwise produce a run of k consecutive equal values in L. 
# For example:
# L = [2, 3, 5, 5, 5, 3] 
# shortenLongRuns(L, 2)
# assert(L == [2, 3, 5, 3])
# And: 
# L = [2, 3, 5, 5, 5, 3]
# shortenLongRuns(L, 3)
# assert(L == [2, 3, 5, 5, 3])
def lookandsay(a):
	# Your code goes here
	l = []
	l1 = []
	if len(a) == 0:
	    return l
	else:
	    i = 0
	    j = 0
	    c = 0
	    l = a
	    while(i < len(a) and j < len(l)):
	        if(a[i] == l[j]):
	            c = c+1
	            j = j + 1
	        else:
	            t = (c,a[i])
	            l1.append(t)
	            i = j
	            c = 0
	    else:
	        t = (c,a[i])
	        l1.append(t)
	    return l1

def destructiveshortenlongruns(L, k):
	l = []
	x = lookandsay(L)
	for i in range(len(x)):
		y = x[i]
		if(y[0]>1 and k <= y[0]):
			for i in range(k-1):
				l.append(y[1])
		else:
			for j in range(y[0]):
				l.append(y[1])
	return l