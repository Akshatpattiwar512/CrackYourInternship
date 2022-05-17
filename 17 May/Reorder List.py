# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        deque = collections.deque()
        point = head
        while point:
            deque.append(point)
            point = point.next
        ptr = dummy = ListNode()
        is_left = True
        while deque:
            if is_left:
                ptr.next = deque.popleft()
            else:
                ptr.next = deque.pop()
            ptr = ptr.next
            is_left = not is_left
        ptr.next = None
        dummy.next = None
