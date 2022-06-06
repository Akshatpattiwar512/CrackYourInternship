# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        leftCnt = self.Count(root.left)
        if leftCnt == k - 1:
            return root.val
        if leftCnt > k - 1:
            return self.kthSmallest(root.left, k)
        return self.kthSmallest(root.right, k - leftCnt - 1)
    
    def Count(self, node: TreeNode):
        if not node:
            return 0
        return 1 + self.Count(node.left) + self.Count(node.right)
