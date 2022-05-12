# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

class Solution:
    def isHappy(self, n: int) -> bool:
        return self.isHappyRecursive(n, {})
    def isHappyRecursive(self, n: int, cache):
        digits = [int(c) for c in str(n)]
        squared = [i ** 2 for i in digits]
        total = sum(squared)
        if total == 1:
            return True
        if total in cache:
            return False
        cache[total] = True
        return self.isHappyRecursive(total, cache)
