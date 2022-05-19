# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the 
# ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

class Solution:
    def dailyTemperatures(self, a: List[int]) -> List[int]:
        n = len(a)
        res = [0]*n
        s = deque()
        i = 0
        while i<n:
            if not s or a[i] <= a[s[-1]]:
                s.append(i)
                i+=1
                continue
            t = s.pop()
            res[t] = i-t
        return res
