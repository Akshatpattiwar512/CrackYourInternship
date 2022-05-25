# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:

# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if self.solve(root)!=-1:
            return True
        return False
    def solve(self,root):
        if root is None:
            return 0
        lh=self.solve(root.left)
        rh=self.solve(root.right)
        if lh==-1 or rh==-1:
            return -1
        if abs(lh-rh)>1:
            return -1
        return max(lh,rh)+1
        
