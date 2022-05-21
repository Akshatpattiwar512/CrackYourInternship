# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
class Solution:
    def isSymmetric(self, root):
        def isSymmetricHelper(left, right):
            return left and right and left.val == right.val and isSymmetricHelper(left.left, right.right) and isSymmetricHelper(left.right, right.left) or left is right
        if not root:
            return True
        return isSymmetricHelper(root.left, root.right)
