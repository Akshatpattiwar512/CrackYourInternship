# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        def helper(root, depth):
            if not root:
                return 0
            if not root.left and not root.right:
                depth += 1
            left = 1 + helper(root.left, depth)
            right = 1 + helper(root.right, depth)
            return max(left, right)
        return helper(root, depth)
