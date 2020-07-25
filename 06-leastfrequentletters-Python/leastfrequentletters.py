# leastFrequentLetters(s) [20 pts]
# Write the function leastFrequentLetters(s), that takes a string s, and ignoring case (so "A" and "a" are treated 
# the same), returns a lowercase string containing the least-frequent alphabetic letters that occur in s, each 
# included only once in the result and then in alphabetic order. So:
# leastFrequentLetters("aDq efQ? FB'daf!!!") 
# returns "be". Note that digits, punctuation, and whitespace are not letters! Also note that seeing as we have not 
# yet covered lists, sets, maps, or efficiency, you are not expected to write the most efficient solution. Finally, 
# if s does not contain any alphabetic characters, the result should be the empty string ("")

def leastfrequentletters(s):
	res = ""
	st = ""
	d = {}
	min = 10
	for i in s:
		if((i>='a' and i<= 'z') or (i>='A' and i<='Z')):
			res += i.lower()
	for i in res:
		c = res.count(i)
		d[i] = c
		if(c < min):
			min = c
	for i in d:
		if(d[i] == min):
			st += i
	l = sorted(st)
	st = "".join(l)
	return st
