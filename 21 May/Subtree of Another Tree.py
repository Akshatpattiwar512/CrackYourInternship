# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def isEqual(n1, n2):
            if n1 and n2:
                return n1.val == n2.val and isEqual(n1.left, n2.left) and isEqual(n1.right, n2.right)
            elif any([n1, n2]):
                return False
            else:
                return True
        def dfs(n1, n2):
            if n1 and n2:
                if n1.val == n2.val and isEqual(n1, n2):
                    return True
                return dfs(n1.left, n2) or dfs(n1.right, n2)
            elif any([n1, n2]):
                return False
            else:
                return True
        return dfs(s, t)
