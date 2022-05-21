# Given the root of a binary tree, invert the tree, and return its root.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return None
        q = [root]
        while q:
            n = q.pop(0)
            n.left, n.right = n.right, n.left
            if n.left: q.append(n.left)
            if n.right: q.append(n.right)
        return root
