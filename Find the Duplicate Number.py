class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            num_idx = abs(nums[i])
            nums[num_idx] *= -1
            if nums[num_idx] > 0:
                return num_idx
