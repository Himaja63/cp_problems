# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g. 
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is 
# "XYZ" and "YXZ" then return false.


def isrotated(str1, str2):
	#Your code goes here
	l = str2.split(str1[-1])
	s = l[1]+l[0]+str1[-1]
	if(s == str1):
		return True
	elif(str2 == str1[::-1]):
		return True
	else:
		return False