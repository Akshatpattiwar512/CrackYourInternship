# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        triplets = []
        for i in range(len(nums)):
            lPoint = i + 1
            rPoint = len(nums) - 1  
            while rPoint > lPoint:
                sum = nums[i] + nums[lPoint] + nums[rPoint]
                if sum == 0:
                    if [nums[i], nums[lPoint], nums[rPoint]] not in triplets:
                        triplets.append([nums[i], nums[lPoint], nums[rPoint]])
                    lPoint += 1
                    rPoint -= 1
                elif sum > 0:
                    rPoint -= 1
                else :
                    lPoint += 1
        return triplets
