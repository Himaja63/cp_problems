# fixMostlyMagicSquare(L) [15 pts]
# In this week's writing session, we wrote isMostlyMagicSquare(L). Here, say we have a mostly magic square L, but 
# then we modify L by changing exactly one value in L so that it no longer is a mostly magic square. For this 
# exercise, we assume we have just such a list L, and your task is to find and fix that change. So, given the list 
# L, return a new list M such that M is the same as L, only with exactly one value changed, and M is a mostly magic 
# square.

def lookandsay(a):
	# Your code goes here
	l = []
	l1 = []
	if len(a) == 0:
	    return l
	else:
	    i = 0
	    j = 0
	    c = 0
	    l = a
	    while(i < len(a) and j < len(l)):
	        if(a[i] == l[j]):
	            c = c+1
	            j = j + 1
	        else:
	            t = (c,a[i])
	            l1.append(t)
	            i = j
	            c = 0
	    else:
	        t = (c,a[i])
	        l1.append(t)
	    return l1
def oddOneOut(l):
    l1 = lookandsay(l)
    for i in l1:
	    if i[0] == 1:
	        res = i[1]
    return res

def getIndex(l):
    n = oddOneOut(l)
    for i in range(len(l)):
        if (l[i] == n):
            res = i
            break
    return res
    
def sameNum(l):
	n = oddOneOut(l)
	arr = []
	for i in range(len(l)):
		if (l[i] != n):
			arr.append(l[i])
	return list(set(arr))

def fixmostlymagicsquare(L):
	l1 = []	
	l2 = []
	arr = []
	add = 0
	for i in range(len(L)):
		sum = 0
		for j in range(len(L)):
			sum = sum + L[i][j]
		l1.append(sum)

	for i in range(len(L)):
		sum = 0
		for j in range(len(L)):
			sum = sum + L[j][i]
		l2.append(sum)
	row = getIndex(l1)
	col = getIndex(l2)
	num = sameNum(l1)[0]
	for i in range(len(L)):
		if i != col:
			add = add + L[row][i]
# 	print(num)
# 	print(add)
	ans = num - add
# 	print(ans)
	L[row][col] = ans
	return L
		
	