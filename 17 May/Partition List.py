# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        before = beforeh = ListNode(0)
        after = afterh = ListNode(0)
        node = head
        while node:
            #print (node.val)
            if node.val < x:
                before.next = node
                before = before.next
                #print ('Node2', node2)
            else:
                after.next = node
                after = after.next
                #print ('Node 1',node1)
            node= node.next
        after.next = None
        before.next = afterh.next
        #print (beforeh.next)
        return beforeh.next
