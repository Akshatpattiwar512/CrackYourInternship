# You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        lis = []
        self.inorder(lis,root)
        x,y = self.findswap(lis)
        x.val,y.val = y.val,x.val
        
    def findswap(self,lis):
        i = 0
        x = None
        y = None
        while i < len(lis)-1:
            if lis[i+1].val < lis[i].val:
                y = lis[i+1]
                if x == None:
                    x = lis[i]
                else:
                    break
            i += 1
        return x,y
     
    def inorder(self,lis,root):
        if root == None:
            return
        self.inorder(lis,root.left)
        lis.append(root)
        self.inorder(lis,root.right)
