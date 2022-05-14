# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return
        current = head
        if current:
            while current.next and current:
                # print(current.val)
                if current.val == current.next.val:
                    current.next = current.next.next
                else:
                    current= current.next
        return head
        
