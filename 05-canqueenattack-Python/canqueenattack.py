# canQueenAttack(qX, qY, oX, oY) [15 pts]
# Given the position of the queen (qX, qY) and the opponent (oX, oY) on a chessboard. The task is to determine 
# whether the queen can attack the opponent or not. Note that the queen can attack in the same row, same column and 
# diagonally.

# def diag(qR, qC, oR, oC):
# 	if (qC == qR+1 and oR == qC+1 and oC == oR+1):
# 		return True
# 	else:
# 		return False

def canqueenattack(qR, qC, oR, oC):
	# Your code goes here
	row = []
	col = []
	l = []
	for j in range(qC+1, 9):
		col.append(j)
	for i in range(qR+1, qR+1+len(col)):
		row.append(i)
	for k in range(len(row)):
		t = (row[k], col[k])
		l.append(t)
	if (oR, oC) in l:
		return True
		
	elif(qR == oR or qC == oC):
		return True
	else:
		return False
	