# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head and head.next:
            head.val, head.next.val = head.next.val, head.val
            head.next.next = self.swapPairs(head.next.next) 
        return head
