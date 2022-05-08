# Given an integer array nums, return the number of reverse pairs in the array.
# A reverse pair is a pair (i, j) where 0 <= i < j < nums.length and nums[i] > 2 * nums[j].

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        res = 0
        arr = []
        for j in range(len(nums)):
            index = bisect.bisect_right(arr, 2*nums[j])
            res+=len(arr)-index
            bisect.insort(arr, nums[j])
        return res
