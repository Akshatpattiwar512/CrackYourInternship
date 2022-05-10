# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

class Solution:
    def validPalindrome(self, s):
        def isPalindrome(s, i, j, deleted):
            while i < j:
                if s[i] != s[j]: 
                    return not deleted and (isPalindrome(s, i+1, j, True) or isPalindrome(s, i, j-1, True))
                i, j = i+1, j-1
            return True
        
        return isPalindrome(s, 0, len(s)-1, False)
