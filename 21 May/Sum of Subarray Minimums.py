#Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

class Solution:
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        minQueue = []
        dp = [a for a in A]
        for i,a in enumerate(A):
            if i >0:
                while minQueue and minQueue[-1][0] > a:
                    minQueue.pop()
                if not minQueue:
                    index = -1
                else:
                    index = minQueue[-1][1]
                dp[i] += dp[i-1] + (i-index-1)*a
                if index>=0:
                    dp[i] += dp[index]
                if index >0:
                    dp[i] -= dp[index-1]
            minQueue.append((a,i))
        return dp[len(A)-1]%(10**9+7)
