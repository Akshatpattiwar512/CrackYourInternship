# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.

class Solution:
    def isPowerOfTwo(self, n):
        if n < 1:
            return False
        while not n%2:
            n /= 2
        return n==1
