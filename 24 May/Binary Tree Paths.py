# Given the root of a binary tree, return all root-to-leaf paths in any order.

# A leaf is a node with no children.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
class Solution:
    def binaryTreePaths(self, root):
        ans = []
        def dfs(r, tmp):
            if r.left:
                dfs(r.left, tmp + [str(r.left.val)])
            if r.right:
                dfs(r.right, tmp + [str(r.right.val)])
            if not r.left and not r.right:
                ans.append('->'.join(tmp))
        if not root:
            return []
        dfs(root, [str(root.val)])
        return ans
