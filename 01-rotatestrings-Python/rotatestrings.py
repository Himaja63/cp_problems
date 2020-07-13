# Write the function rotatestring(s, k) that takes a string s and a possibly-negative integer k. 
# If k is non-negative, the function returns the string s rotated k places to the left. 
# If k is negative, the function returns the string s rotated |k| places to the right. So, for example:
# assert(rotateString('abcd',  1) == 'bcda')
# assert(rotateString('abcd', -1) == 'dabc')



def fun_rotatestrings(s, n):
	l = len(s) + 1
	str = ""
	if(abs(n) < l):
		if (n > 0):
			a = s[0:n]
			b = s[n:]		
			str = b + a
		elif (n < 0):
			a = s[n:]
			b = s[0:n]		
			str = a + b
	elif(abs(n) > l):
		if (n < 0):
			n = n + l
			a = s[n:]
			b = s[0:n]		
			str = a + b
		elif(n > 0):
			n = n - l
			a = s[0:n]
			b = s[n:]		
			str = b + a
			
	return str

