# Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal 
# of the same tree, reconstruct and return the binary tree.

# If there exist multiple answers, you can return any of them.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if len(pre) == 0 or len(post) == 0:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        currentRootValue = pre[0]
        subTreeRootValue = pre[1]
        subTreeRootIdx = post.index(subTreeRootValue)
        leftSubTree = None
        rightSubTree = None
        if subTreeRootIdx == len(post) - 2:
            rightSubTree = self.constructFromPrePost(pre[1:], post[:-1])
        else:
            leftSubTree = self.constructFromPrePost(pre[1:subTreeRootIdx + 2], post[:subTreeRootIdx + 1])
            rightSubTree = self.constructFromPrePost(pre[subTreeRootIdx + 2:], post[subTreeRootIdx + 1:-1])
        return TreeNode(currentRootValue, leftSubTree, rightSubTree)
