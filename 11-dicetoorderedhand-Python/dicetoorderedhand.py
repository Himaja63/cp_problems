# dicetoorderedhand(a, b, c) [5pts]
# Write the function dicetoorderedhand(a, b, c) that takes 3 dice and
# returns them in a hand, which is a 3-digit integer. However, even if the
# dice are unordered, the resulting hand must be ordered so that the largest
# die is on the left and smallest die is on the right. For example:
# assert(dicetoorderedhand(1,2,3) == 321)
# assert(dicetoorderedhand(6,5,4) == 654)
# assert(dicetoorderedhand(1,4,2) == 421)
# assert(dicetoorderedhand(6,5,6) == 665)
# assert(dicetoorderedhand(2,2,2) == 222)
# Hint: You can use max(a,b,c) to find the largest of 3 values, and
# min(a,b,c) to find the smallest.

def dicetoorderedhand(a, b, c):
	if (a == b == c):
		return int(str(a)+str(b)+str(c))
	elif (a == b and c != a):
		if (a > c):
			return int(str(a)+str(b)+str(c))
		else:
			return int(str(c)+str(a)+str(b))
	elif(b == c and a != b):
		if (b > a):
			return int(str(b)+str(c)+str(a))
		else:
			return int(str(a)+str(b)+str(c))
	elif (a == c and b != a):
		if (a > b):
			return int(str(a)+str(c)+str(b))
		else:
			return int(str(b)+str(a)+str(c))
	
	else :		
		l = []
		l.append(a)
		l.append(b)
		l.append(c)
		t = tuple(l)
		ma = max(t)
		mi = min(t)
		for i in t:
			if (i != ma and i != mi):
				mid = i
		s = str(ma)+str(mid)+str(mi)
		return int(s)
