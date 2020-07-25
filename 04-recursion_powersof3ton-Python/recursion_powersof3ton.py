# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the 
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers 
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem. 

def recursion_powersof3ton(n):
	# Your code goes here
	n=int(n)
	if n<=0:
		return None
	if n==1:
		return [1] 
	else:
		if 1162261467 % n ==0:
			return sorted([n]+recursion_powersof3ton(n-1))
		else:
			return recursion_powersof3ton(n-1)