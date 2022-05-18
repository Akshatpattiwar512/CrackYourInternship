# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0 : return None
        ls =[]
        for oneList in lists:
            while oneList:
                ls.append(oneList.val)
                oneList = oneList.next
        ls.sort()
        head = dumphead = ListNode(None)
        for one in ls:
            head.next = ListNode(one)
            head = head.next
        return dumphead.next
        
