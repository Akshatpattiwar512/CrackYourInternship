# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        listA=[]
        listB=[]
        cur=l1
        while(cur):
            listA.append(str(cur.val))
            cur=cur.next
        cur=l2
        listA.reverse()
        while(cur):
            listB.append(str(cur.val))
            cur=cur.next
        listB.reverse()
        totalSum= int("".join(listA)) + int("".join(listB))
        splitSum= [int(d) for d in str(totalSum)]
        splitSum.reverse()
        dummy=ListNode(0)
        cur=dummy
        for num in splitSum:
            cur.next=ListNode(num)
            cur=cur.next
        return dummy.next
        
        
