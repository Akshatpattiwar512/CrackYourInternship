# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes 
# is not a multiple of k then left-out nodes, in the end, should remain as it is.

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
class Solution:
    def reverse(self, head):
        if not head: return None, None
        if not head.next: return head, head
        tail, f, r = head, head.next, None
        while f:
            head.next = r
            r = head
            head = f
            f = f.next
        head.next = r
        return head, tail
    def reverseKGroup(self, head, k):
        if not head: return None
        if not head.next or k < 2: return head
        h = t = head
        prv, nxt = None, None
        #     [1->2->3]->[4->5->6]->[7->8]
        #     [3->2->1]->[6->5->4]->[7->8]
        # prv  h     t   nxt
        while True:
            for _ in range(k-1): 
                if t.next: 
                    t = t.next
                else:
                    return head
            nxt = t.next
            t.next = None
            h, t = self.reverse(h)
            if not prv:
                head = h
            else:
                prv.next = h
            if not nxt:
                return head
            prv = t
            t.next = nxt
            h = t = nxt
