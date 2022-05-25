# Given the root of a binary tree, return the inorder traversal of its nodes' values.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def helper(node, lst):
            if not node: return
            helper(node.left, lst)
            lst.append(node.val)
            helper(node.right, lst)
        lst = []
        helper(root, lst)
        return lst
