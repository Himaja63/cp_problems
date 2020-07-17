# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both 
# guaranteed to not contain any 0's, and 
# returns True if x is a rotation of the digits of y and False otherwise. For example, 
# 3412 is a rotation of 1234. Any number 
# is a rotation of itself.

def isrotation(x, y):
	d = 0
	flag = 0
	s1 = str(x)
	s2 = str(y)
	r = ""
	if (len(s1) == len(s2)):
		while (d < len(s1)):
			r1 = s1[0 : len(s1)-d]
			r2 = s1[len(s1)-d : ]
			r = r2+r1
			if (r == s2):
				flag = 1
				break
			d = d+1
		if (flag == 1):
			return True
		elif(s2 == s1[::-1]):
			return True
		else:
			return False
	else:
		return False
