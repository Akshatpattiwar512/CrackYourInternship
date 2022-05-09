# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        min_length = min(len(s) for s in strs)
        prefix = ''
        for i in range(min_length):
            c = strs[0][i]
            for s in strs:
                if s[i] != c:
                    return prefix
            prefix += c
        return prefix
