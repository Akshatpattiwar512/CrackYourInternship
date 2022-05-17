# Given the head of a linked list, return the list after sorting it in ascending order.

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        l = []
        while cur:
            l.append(cur.val)
            cur = cur.next
        l.sort()
        ans = node = ListNode(0)
        for i in range(len(l)):
            node.next = ListNode(l[i])
            node = node.next
        return ans.next
