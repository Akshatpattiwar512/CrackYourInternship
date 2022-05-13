# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

from math import gcd
from collections import Counter
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def slope(p, q):
            dx, dy = q[0] - p[0], q[1] - p[1]
            if dx == 0: 
                return 'inf_or_same'
            if dx < 0:
                dx, dy = -dx, -dy
            g = gcd(dx, dy)
            return (dx/g, dy/g)
        ans = 0
        for i, p in enumerate(points):
            duplicates = 0
            lines = Counter()
            for q in points[i:]:
                duplicates += p == q
                lines[slope(p, q)] += 1 
            lines['inf_or_same'] -= duplicates
            max_lines_through_point = max(lines.values()) + duplicates
            ans = max(ans, max_lines_through_point)
        return ans
