# Write the function rotatestring(s, k) that takes a string s and a possibly-negative integer k. 
# If k is non-negative, the function returns the string s rotated k places to the left. 
# If k is negative, the function returns the string s rotated |k| places to the right. So, for example:
# assert(rotateString('abcd',  1) == 'bcda')
# assert(rotateString('abcd', -1) == 'dabc')



def fun_rotatestrings(s, n):
	l = len(s)
	str = ""
	if(abs(n) < l):
		if (n > 0):
			s1 = s[0:n]
			s2 = s[n:]		
			str = s2 + s1
		elif (n < 0):
			s1 = s[n:]
			s2 = s[0:n]		
			str = s1 + s2
	elif(abs(n) > l):
		if (n < 0):
			n = n + l
			s1 = s[n:]
			s2 = s[0:n]		
			str = s1 + s2
		elif(n > 0):
			n = n - l
			s1 = s[0:n]
			s2 = s[n:]		
			str = s2 + s1
	else:
		str = s			
	return str

