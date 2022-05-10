# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution(object):
    def groupAnagrams(self, strs):
        d = {}
        for string in sorted(strs):
            s = "".join(sorted(string))
            d[s] = d.get(s, []) + [string]
        return [l for l in d.values()]
