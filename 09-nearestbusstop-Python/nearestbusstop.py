# Write the function nearestBusStop(street) that takes a 
# non-negative int street number, and returns the nearest 
# bus stop to the given street, where buses stop every 8th street, 
# including street 0, and ties go to the lower street, 
# so the nearest bus stop to 12th street is 8th street, 
# and the nearest bus stop to 13 street is 16th street.



def fun_nearestbusstop(street):
	n = street / 8
	l = str(n).split('.')
	if (int(l[1][0]) > 5):
		return 8 * (int(l[0])+1)
	else :
		return 8 * (int(l[0]))
	
