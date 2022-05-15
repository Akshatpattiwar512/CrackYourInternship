# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding 
# original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied 
#list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

# Return the head of the copied linked list.

# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        vallist = []
        randomlist = []
        nodeobjdict = {}
        node = head
        while node is not None:
            vallist.append(node.val)
            if node.random is not None:
                randomlist.append(node.random.val)
            else:
                randomlist.append(None)
            node = node.next
        newhead = Node(0,0,0)
        node = newhead
        for val in vallist:
            node.next = Node(val,None,None)
            nodeobjdict[val] = node.next
            node = node.next
        node = newhead
        for r in randomlist:
            if r is not None:
                node.next.random = nodeobjdict[r]
            node = node.next
        return newhead.next
