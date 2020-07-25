# longestCommonSubstring(s1, s2)[20 pts]
# Write the function, longestCommonSubstring(s1, s2), that takes two possibly-empty strings and returns the longest 
# string that occurs in both strings (and returns the empty string if either string is empty). For example:
# longestCommonSubstring("abcdef", "abqrcdest") returns "cde"
# longestCommonSubstring("abcdef", "ghi") returns "" (the empty string)
# If there are two or more longest common substrings, return the lexicographically smaller one (ie, just use "<" to 
# compare the strings). So, for example:
# longestCommonSubstring("abcABC", "zzabZZAB") returns "AB" and not "ab"

def longestcommonsubstring(s1, s2):
    # Yourcode goes here
    ans = ""
    l = []
    max = 0
    if(s1 == "" or s2 == ""):
        return ""
    else:
        for i in range(len(s1)):
            for j in range(len(s2)):
                temp = 0
                res = ""
                while (i+temp < len(s1) and j+temp < len(s2) and s1[i+temp] == s2[j+temp]):
                    res += s2[j+temp]
                    temp += 1
                if(len(res) >= len(ans)):
                    ans = res
                    l.append(ans)
        for i in l:
            if(len(i) >= max):
                ans = i
        return ans
