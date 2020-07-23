# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).

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

def longestdigitrun(n):
	l = lookandsay(list(str(abs(n))))
	max = 0
	res = 0
	lis = []
	for i in l:
		if(i[0] > max):
			max = i[0]
	for i in l:
		if(i[0] == max):
			lis.append(int(i[1]))
	return min(lis)
		

	