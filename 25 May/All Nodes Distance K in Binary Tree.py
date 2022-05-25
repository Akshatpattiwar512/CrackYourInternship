# Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the 
# target node.

# You can return the answer in any order.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
'''
DFS to obtain the parent node for each node
BFS to extend from target node and count distance
'''
class Solution(object):
    def distanceK(self, root, target, K):
        pardict = dict() # node: parent of current node
        
        def dfs(node, par=None):
            if node:
                pardict[node] = par
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)
        
        seen = {target}
        q = collections.deque([(target, 0)])
        while q:
            if q[0][1] == K:
                return [node.val for node, distance in q]
            
            qsize = len(q)
            for _ in range(qsize): # range over all the nodes in current q
                node, distance = q.popleft()
                for nei in (node.left, node.right, pardict[node]):
                    if nei and not nei in seen:
                        q.append((nei, distance + 1))
                        seen.add(nei)
        return []
