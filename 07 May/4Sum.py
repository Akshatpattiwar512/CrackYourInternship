# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # sort 
        nums = sorted(nums)
        res  = set()
        for i, a in enumerate(nums[:-3]):
            for j, b in enumerate(nums[i+1:-2]):
                datas = set()
                new_target = target - a - b
                for d in nums[i+j+2:]:
                    c = new_target - d
                    if c in datas:
                        res.add((a,b,c,d))
                    else:
                        datas.add(d)
        return [list(x) for x in res]
        
