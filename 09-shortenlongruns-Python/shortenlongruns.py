# shortenLongRuns(L, k) [15 pts]
# Write the non-destructive function shortenLongRuns(L, k) that takes a list L and a positive integer k, and 
# non-destructively returns a similar list, only without any run of k consecutive equal values in L. This means that 
# any values that would otherwise produce a consecutive run of k elements are not present. 
# For example: 
# assert(shortenLongRuns([2, 3, 5, 5, 5, 3], 2) == [2, 3, 5, 3]) 
# assert(shortenLongRuns([2, 3, 5, 5, 5, 3], 3) == [2, 3, 5, 5, 3]) 
# Note: your function may not just create a copy of L and call the destructive version of this function (below) on 
# that copy and return it. Instead, you must directly construct the result here.

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


def shortenlongruns(L, k):
	# Your code goes here
	l = []
	x = lookandsay(L)
	for i in range(len(x)):
		y = x[i]
		if (y[0] > 1 and k <= y[0]):
			for i in range(k-1):
				l.append(y[1])
		else:
			for j in range(y[0]):
				l.append(y[1])
	return l
		