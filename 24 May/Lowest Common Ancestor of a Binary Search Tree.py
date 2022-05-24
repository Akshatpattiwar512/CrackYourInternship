# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as 
# descendants (where we allow a node to be a descendant of itself).”

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if q.val<p.val:
            return self.lowestCommonAncestor(root,q,p)
        if p.val<=root.val<=q.val:
            return root
        elif q.val<root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return self.lowestCommonAncestor(root.right,p,q)
