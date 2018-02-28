"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: The first node of linked list.
    @return: The head of linked list.
    """
    def insertionSortList(self, head):
        # write your code here
        if not head:
            return None
        if not head.next:
            return head
        res = ListNode(0)
        while head:
            node = res
            fol = head.next
            while node.next and node.next.val < head.val:
                node = node.next
            head.next = node.next
            node.next = head
            head = fol
        return res.next
            
