# You are given an array points containing the coordinates of points on a 2D plane, sorted by the x-values, 
# where points[i] = [xi, yi] such that xi < xj for all 1 <= i < j <= points.length. You are also given an integer k.

# Return the maximum value of the equation yi + yj + |xi - xj| where |xi - xj| <= k and 1 <= i < j <= points.length.

# It is guaranteed that there exists at least one pair of points that satisfy the constraint |xi - xj| <= k.

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        """ Sliding window with deque solution similar to sliding window
        and queue with max pattern.
        
        Also notice that yi + yj + abs(xi - xj) when i < j is (because xj > xi):
        (yj + xj) + (yi - xi) 
        """
        n = len(points)
        max_s = float('-inf')
        q = collections.deque()
        for j in range(n):
            while q and points[j][0] - points[q[0]][0] > k:
                q.popleft()
            if q:
                i = q[0]
                max_s = max(max_s, points[j][0] + points[j][1] + points[i][1] - points[i][0])
            while q and points[q[-1]][1] - points[q[-1]][0] < points[j][1] - points[j][0]:
                q.pop()
            q.append(j)
        return max_s
