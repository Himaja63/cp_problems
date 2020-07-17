# median(a) (10 pts)
# Write the non-destructive function median(a) that takes a list of ints or floats and returns the median value, 
# which is the value of the middle element, or the average of the two middle elements if there is no single middle 
# element. If the list is empty, return None.

def median(a):
	if (len(a) % 2 == 0):
		x = len(a) / 2
		y = x + 1
		res = (a[x] + a[y])/2
		return res
	elif(len(a) == 0):
		return None
	else:
		x = len(a)//2
		return a[x+1]