# A peak element is an element that is strictly greater than its neighbors.

# Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞.

# You must write an algorithm that runs in O(log n) time.

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        if len(nums) == 2: return nums.index(max(nums))
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r -l ) // 2
            if nums[mid] < nums[mid+1]:
                l = mid + 1
            else:
                r = mid
        return l
