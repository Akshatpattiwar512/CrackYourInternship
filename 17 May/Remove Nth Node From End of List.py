# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None: return head
        empty = ListNode(0)
        empty.next = head
        curr = head
        next = curr
        count = 0
        while curr is not None:
            curr = curr.next
            count +=1
        curr = empty
        for i in range(count - n):
            curr = curr.next
        curr.next = curr.next.next
        return empty.next
