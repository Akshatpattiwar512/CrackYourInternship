# Given two strings s and t, return the number of distinct subsequences of s which equals t.

# A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' 
# relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

# The test cases are generated so that the answer fits on a 32-bit signed integer.

class Solution(object):
    def numDistinct(self, s, t):
        if not t:
            return 1
        nLen = len(t)
        table = [0 for i in range(nLen + 1)]
        idxes = dict()
        table[-1] = 1
        cur = 0
        for i in range(len(s)):
            if cur < nLen:
                if t[cur] == s[i]:
                    if t[cur] not in idxes:
                        idxes[t[cur]] = [cur]
                    else:
                        idxes[t[cur]].append(cur)
                    cur += 1
            if s[i] in idxes:
                for j in idxes[s[i]][::-1]:
                    table[j] += table[j-1]
        return table[nLen-1]
