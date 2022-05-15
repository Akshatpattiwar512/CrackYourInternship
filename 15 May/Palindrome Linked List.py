# Given the head of a singly linked list, return true if it is a palindrome.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
     def isPalindrome(self, head: ListNode) -> bool:
        numList = []
        while head is not None:
            numList.append(head.val)
            head = head.next
        numList2 = numList[::-1]
        if numList2 == numList:
            return True
        else:
            return False
