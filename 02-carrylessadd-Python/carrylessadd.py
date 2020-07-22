# carry less addition means a  normal addition with the carry from each column ignored. 
# So, for example, if we carryless-ly add 8+7, we get 5 (ignore the carry). And if we add 
# 18+27, we get 35 (still ignore the carry). With this in mind, write the function 
# fun_carrylessadd(x, y) that takes two non-negative integers x and y and returns their 
# carryless sum. As the paper demonstrates, fun_carrylessadd(785, 376) returns 51.


def fun_carrylessadd(x, y):
	l1 = list(str(x))
	l2 = list(str(y))
	i = len(l1)-1
	j = len(l2)-1
	res = []
	while(i>=0 or j>=0):
		sum = 0
		if(i>=0 and j >=0):
			sum += int(l1[i]) + int(l2[j])
			if(sum >= 10):
				sum = sum - 10
				res.append(str(sum))
				i = i-1
				j = j-1
			else:
				res.append(str(sum))
				i - i-1
				j = j-1
		else:
			if(i>=0):
				res.append(str(l1[i]))
				i = i-1
			else:
				res.append(str(l2[j]))
				j = j-1
	return int("".join(res[::-1]))
	

