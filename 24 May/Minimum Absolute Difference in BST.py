# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

'''
 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        values = []
        def dfs(node):
            if node.left: dfs(node.left)
            values.append(node.val)
            if node.right: dfs(node.right)
        dfs(root)
        return min(second - first for first, second in zip(values, values[1:]))
