# Given the coordinates of four points in 2D space p1, p2, p3 and p4, return true if the four points construct a square.

# The coordinate of a point pi is represented as [xi, yi]. The input is not given in any order.

# A valid square has four equal sides with positive length and four equal angles (90-degree angles).

import math
class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        distance = set()
        d2 = self.distance(p1,p2)
        d3 = self.distance(p1,p3)
        d4 = self.distance(p1,p4)
        if d2==0 or d3==0 or d4==0:
            return False
        if d2==d3 and 2*d2==d4:
            if self.distance(p2,p4)==self.distance(p3,p4):
                return True
            else:
                return False
        elif d2==d4 and 2*d2==d3:
            if self.distance(p2,p3)==self.distance(p4,p3):
                return True
            return False
        elif d3==d4 and 2*d3==d2:
            if self.distance(p2,p3)==self.distance(p4,p2):
                return True
            return False
        else:
            return False
    def distance(self,p1,p):
        dist = ((p1[0]-p[0])*(p1[0]-p[0])) + ((p1[1]-p[1])*(p1[1]-p[1]))
        return dist
