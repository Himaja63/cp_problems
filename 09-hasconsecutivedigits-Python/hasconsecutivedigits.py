# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly 
# negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	n = abs(n)
	s = str(n)
	flag = 0
	for i in range(len(s) - 1):
		if (s[i] == s[i+1]):
			flag = 1
			break
	if (flag == 1):
		return True
	else:
		return False

