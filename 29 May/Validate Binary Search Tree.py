# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
class Solution:
    def isValidBST(self, tree: TreeNode, minimum = float("-inf"), maximum = float("inf")) -> bool:
        if tree is None:
            return True
        if tree.val <= minimum or tree.val >= maximum:
            return False
        leftIsValid = self.isValidBST(tree.left, minimum, tree.val)
        rightIsValid = self.isValidBST(tree.right, tree.val, maximum)
        return leftIsValid and rightIsValid
