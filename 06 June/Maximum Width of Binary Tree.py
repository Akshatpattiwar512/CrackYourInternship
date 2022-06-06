# Given the root of a binary tree, return the maximum width of the given tree.

# The maximum width of a tree is the maximum width among all levels.

# The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

# It is guaranteed that the answer will in the range of a 32-bit signed integer.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
from collections import defaultdict
class Solution:
    def widthOfBinaryTree(self, root):
		
        def helper(node, pos, level):
            if node is None:
                return 0
            lmap[level] = (min(lmap[level][0], pos), max(lmap[level][1], pos))
            return max(
                lmap[level][1]-lmap[level][0]+1,
                helper(node.left, pos*2, level+1),
                helper(node.right, pos*2 + 1, level+1))
        
        lmap = defaultdict(lambda : (float('inf'), -float('inf')))
        return helper(root, 0, 0)
