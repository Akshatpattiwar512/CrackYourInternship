# Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.
# A subarray is a contiguous part of an array.

class Solution:
    def subarraysDivByK(self, A: List[int], k: int) -> int:
        dic = collections.defaultdict(int)
        dic[0] = 1
        ans = 0
        presum = 0
        for num in A:
            presum += num
            ans += dic[presum%k]
            dic[presum%k] += 1
        return ans
