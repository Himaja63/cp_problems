# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.
import math
def fun_distance(x1, y1, x2, y2):
	# your code goes here
	a = (x2-x1)**2
	b = (y2-y1)**2
	d = math.sqrt(a + b)
	return int(d)

def isrighttriangle(x1, y1, x2, y2, x3, y3):
	# your code goes here
	s1 = fun_distance(x1, y1, x2, y2)
	s2 = fun_distance(x2, y2, x3, y3)
	s3 = fun_distance(x3, y3, x1, y1)
	sum1 = s1**2 + s2**2
	# sum2 = s2**2 + s3**2
	# sum3 = s3**2 + s1**2
	if (math.isclose(sum1, s3**2)):
		return True
	else:
		return False
