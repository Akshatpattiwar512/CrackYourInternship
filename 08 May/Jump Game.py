# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxi=0
        maxIndex=0
        c=1
        i=-1
        while c and i<len(nums)-1:
            i+=1
            c-=1
            c= max(c, nums[i])
            
        print(i)
        return i>=len(nums)-1
