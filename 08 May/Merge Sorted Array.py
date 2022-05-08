# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, 
# where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        ptr1 = m-1
        ptr2 = n-1
        
        masterptr = m+n-1
        
        while masterptr > -1 and ptr1 > -1 and ptr2 > -1:
            if nums1[ptr1] > nums2[ptr2]:
                nums1[masterptr] = nums1[ptr1]
                ptr1 -= 1
            else:
                nums1[masterptr] = nums2[ptr2]
                ptr2 -= 1
            masterptr -= 1
        
        while ptr2 > -1:
            nums1[masterptr] = nums2[ptr2]
            ptr2 -= 1
            masterptr -= 1
