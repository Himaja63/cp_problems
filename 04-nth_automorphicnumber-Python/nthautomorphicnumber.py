# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the 
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6, 
# 76 and 890625 are all automorphic numbers.

def nthautomorphicnumbers(n):
	c = 0
	i = 0
	while(c<n):
		sqr = i**2
		s = str(sqr)
		if(s[len(s)-len(str(i)):] == str(i)):
			c = c+1
			i = i+1
		else:
			i = i+1
	return i - 1