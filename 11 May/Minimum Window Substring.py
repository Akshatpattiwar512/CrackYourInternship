# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. 
# If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# A substring is a contiguous sequence of characters within the string.

class Solution(object):
    def minWindow(self, s, t):
        need = collections.Counter(t)
        missing = len(t)
        start,end = 0,len(s)
        i = 0
        for j,c in enumerate(s):
            if need[c] > 0:
                missing -= 1
            need[c] -= 1
            if missing == 0:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if j - i < end - start:
                    start,end = i,j
                need[s[i]] += 1
                missing += 1
                i += 1
        return s[start:end+1] if end - start < len(s) else ''
