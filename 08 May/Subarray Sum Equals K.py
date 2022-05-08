# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hsh = {0: 1}
        sm  = 0
        op = 0
        # keep track of sum at every index and store the frequency in a hash map
        for num in nums:
            sm+=num
            # if sum-k is already in hashmap
            # that means there exist hsh[sm-k] sub arrays that has sum k
            if sm-k in hsh:
                op+=hsh[sm-k]
            hsh[sm] = hsh.get(sm,0)+1
        return op
