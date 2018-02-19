# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def merge(self, l1, l2):
        s = t = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                t.next, t, l1 = l1, l1, l1.next
            else:
                t.next, t, l2 = l2, l2, l2.next
        t.next = l1 or l2
        return s.next
            
            
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:return head
        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None
        return self.merge(self.sortList(head), self.sortList(slow))
