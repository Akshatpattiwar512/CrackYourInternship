#Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return 
# null.



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        n1, n2 = headA, headB
        while n1 != n2:
            n1 = n1.next if n1 != None else headB
            n2 = n2.next if n2 != None else headA
        return n1
