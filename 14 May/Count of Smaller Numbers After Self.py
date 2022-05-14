# You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to 
# the right of nums[i].

import bisect
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sortedL, res = [], []
        for n in nums[:: -1]:
            idx = bisect.bisect_left(sortedL, n)
            sortedL.insert(idx, n)
            res.append(idx)
        return res[::-1]
