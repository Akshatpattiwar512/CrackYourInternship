# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list 
# sorted as well.

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
class Solution(object):
    def deleteDuplicates(self, head):
        root = ListNode(0)
        root.next = head
        head = root
        while head:
            while head.next and head.next.next and head.next.next.val == head.next.val:
                curr = head.next
                while curr and curr.val == head.next.val:
                    curr = curr.next
                head.next = curr
            head = head.next
        return root.next
