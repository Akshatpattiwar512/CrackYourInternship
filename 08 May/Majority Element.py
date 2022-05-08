# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=len(nums)/2
        num_dict={}
        for i in range(len(nums)):
            if nums[i] in num_dict.keys():
                num_dict[nums[i]]+=1
            else:
                num_dict[nums[i]]=1
        for key in num_dict:
            if num_dict[key] > count:
                return key
