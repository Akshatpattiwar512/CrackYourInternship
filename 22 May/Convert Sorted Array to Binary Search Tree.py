# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
class Solution:
    def helper(self, nums, start, stop):
        if (stop < start or start >= stop):
            return None
        mid = start + (stop - start)//2
        node = TreeNode(nums[mid])
        node.left = self.helper(nums, start, mid)
        node.right = self.helper(nums, mid+1, stop)
        return node
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        return self.helper(nums, 0, len(nums))
