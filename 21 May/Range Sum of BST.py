# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        res = 0
        if root:
            if L<= root.val <= R:
                res += root.val
            if root.val > L:
                res += self.rangeSumBST(root.left, L, R)
            if root.val < R:
                res += self.rangeSumBST(root.right, L, R)
        return res
