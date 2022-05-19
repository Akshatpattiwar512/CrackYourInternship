# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

''' 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
class Solution(object):
    def diameterOfBinaryTree(self, root):
        def count(root, res):
            if not root:
                return 0,res
            lh,lr = count(root.left, res)
            rh,rr = count(root.right, res)
            return 1+max(lh, rh), max(lr, rr, lh+rh)
        _,res = count(root, 0)
        return res
