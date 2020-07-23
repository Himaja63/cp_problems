# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def property309(n):
    res = n**5
    s = str(res)
    if '0' in s:
        if '1' in s:
            if '2' in s:
                if '3' in s:
                    if '4' in s:
                        if '5' in s:
                            if '6' in s:
                                if '7' in s:
                                    if '8' in s:
                                        if '9' in s:
                                            return True
                                        else:
                                            return False
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


def nthwithproperty309(n):
	c = 0
	i = 309
	while(c <= n):
		if (property309(i)):
			c = c+1
			i = i+1
		else:
			i = i+1

	return i-1