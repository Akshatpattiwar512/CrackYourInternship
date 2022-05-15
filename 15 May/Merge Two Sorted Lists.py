# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        dummy= ListNode()
        head=dummy
        if l1 is None:
            dummy.next=l2
        elif l2 is None:
            dummy.next=l1
        while l1 and l2 is not None:
            if l1.val <= l2.val:
                dummy.next=l1
                l1=l1.next
            else:
                dummy.next = l2
                l2=l2.next
            dummy=dummy.next
            if l1 is not None:
                dummy.next = l1
            else:
                dummy.next = l2;
        return head.next
