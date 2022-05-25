# Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n < 1: return []
        nums = list(range(1,n+1))
        return self.helper(nums)
    def helper(self, nums):
        if not nums:
            return [None]
        res = []
        for i in range(len(nums)):
            l = self.helper(nums[:i])
            r = self.helper(nums[i+1:])
            for ltree in l:
                for rtree in r:
                    root = TreeNode(nums[i])
                    root.left = ltree
                    root.right = rtree
                    res.append(root)
        return res 
