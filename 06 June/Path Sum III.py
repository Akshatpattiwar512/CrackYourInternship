# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

# The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.res = 0
        self.target = sum
        self.helper(root)
        return self.res
    def helper(self, root):
        if root:
            dic = {root.val: 1}
            ldic, rdic = self.helper(root.left), self.helper(root.right)
            for d in (ldic, rdic):
                if d:
                    for k in d:
                        if k + root.val not in dic:
                            dic[k+root.val] = 0
                        dic[k+root.val] += d[k]
            self.res += dic[self.target] if self.target in dic else 0
            return dic
        return None
