# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

'''
 Definition for singly-linked list.
 class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
class Solution:
    def addTwoNumbers(self, first: ListNode, second: ListNode) -> ListNode:
        link1 = ''
        link2 = ''
        while first:
            link1 += str(first.val)
            first = first.next
        while second:
            link2 += str(second.val)
            second = second.next
        total = str(int(link1)+int(link2))
        curr = ListNode(0)
        dummy = ListNode(0)
        curr = dummy
        for i in total:
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next
