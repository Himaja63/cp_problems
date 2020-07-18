# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.



def fun_kth_occurrences(s, n):
	d = {}
	l = []
	l1 = []
	for i in s:
		c = s.count(i)
		d[i] = c
		l.append(c)
	l = list(set(l))
	l = l[::-1]
	for i in d:
		if (d[i] == l[n-1]):
			l.append(i)
	return l1[0]


