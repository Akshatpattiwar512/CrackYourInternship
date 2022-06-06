# Given the root of a binary tree, flatten the tree into a "linked list":

# The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
# The "linked list" should be in the same order as a pre-order traversal of the binary tree.

'''
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # preorder: root -> left -> right
        # root, flatten(left), flatter(right)
        # root.right = flatten(left).right = flatter(right)
        if not root:
            return None
        left_flat = self.flatten(root.left)
        right_flat = self.flatten(root.right)
        
        root.left = None
        root.right = None
        
        # do we have left and right children?
        if left_flat:
            # find the tail of left_flat
            tail = left_flat
            while tail.right:
                tail = tail.right
            tail.right = right_flat
            root.right = left_flat
        elif right_flat:
            root.right = right_flat
            
        return root
