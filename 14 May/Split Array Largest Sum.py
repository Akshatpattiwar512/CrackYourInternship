# Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.

# Write an algorithm to minimize the largest sum among these m subarrays.

class Solution:
    def numberSplits(self, nums, target):
        rs = 0
        s = 0
        for num in nums:
            rs += num
            if rs > target:
                rs = num
                s += 1
        return s
    def splitArray(self, nums: List[int], m: int) -> int:
        min_num, max_num = max(nums), sum(nums)
        left, right = min_num, max_num
        while(left <= right):
            pivot = left + (right - left)//2
            n_splits = self.numberSplits(nums, pivot)
            if n_splits < m:
                right = pivot - 1
            else:
                left = pivot + 1
        return left 
