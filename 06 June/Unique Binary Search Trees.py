# Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        mem = {0:1}     
        def solve(n):
            if n in mem:
                return mem[n]
            else:
                num = 0
                for i in range(1,n+1):
                    num += solve(i-1)*solve(n-i)
                mem[n] = num
                return num
        if n==0:
            return 0
        else:
            solve(n)
            return mem[n]
