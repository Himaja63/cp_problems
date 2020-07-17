# removeDuplicate(text) [10 pts]
# Write a program to remove all the duplicate characters from a given input String,e.g.
# if given String is "JavaPython" then the output should be "JavPython".
# The second or further occurrence of duplicate should be removed.

def removeduplicate(text):
	l = list(text)
	l1 = []
	for i in l:
		if i not in l1:
			l1.append(i)
	s = "".join(l1)
	return s