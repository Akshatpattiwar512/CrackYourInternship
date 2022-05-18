# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater
# element, then the answer for this query is -1.


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        stack.append(0)
        dic = {}
        for i in range(1, len(nums2)):
            while stack and nums2[i]>nums2[stack[-1]]:
                idx = stack.pop()
                dic[nums2[idx]] = nums2[i]
            stack.append(i)
        res = []
        for num in nums1:
            if num in dic:
                res.append(dic[num])
            else:
                res.append(-1)
        return res
