# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward.

class Solution:
    def isPalindrome(self, x: 'int') -> 'bool':
        s = str(x)
        s_list = list(s)
        reverse_s = ''
        for i in range(0,len(s_list)):
            reverse_s += s_list.pop()
        if s == reverse_s:
            return True
        else:
            return False
