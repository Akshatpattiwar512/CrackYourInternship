# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        dummy = ListNode() 
        prev_temp = dummy 
        dummy.next = head
        temp = head
        
        while temp:
            if temp.val == val:
                prev_temp.next = temp.next
            else:    
                prev_temp = temp
            temp = temp.next
        
        return dummy.next
