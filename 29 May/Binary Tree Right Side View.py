# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the 
# nodes you can see ordered from top to bottom.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        # BFS, add the node at the end
        # of the level
        queue = [root]
        result = []
        
        while queue:
            result.append(queue[-1].val)
            for _ in range(len(queue)):
                curr = queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        
        return result
