# Write the function isrectangular(L) that takes a possibly-2d 
# list L and returns True  if it is rectangular, so each row has
#  the same number of elements. Return False otherwise.


def fun_isrectangular(l):
	t = len(l[0])
	flag = 0
	for i in l:
		if len(i) != t:
			flag = 1
	if flag == 1:
		return False
	return True

