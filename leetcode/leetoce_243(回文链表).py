# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p1 = p2 = head
        res = None
        while p1 and p1.next:
            p1 = p1.next.next
            res, res.next, p2 = p2, res, p2.next
        if p1:
            p2 = p2.next
        while res and res.val == p2.val:
            res, p2 = res.next, p2.next
        return not res
        
