class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        if m == n:
            return head
        
        for _ in range(m-1):
            pre = pre.next
            
        res = None
        cur = pre.next
        for _ in range(n-m+1):
            next = cur.next
            cur.next = res
            res = cur
            cur = next
        pre.next.next = cur
        pre.next = res
        
        return dummy.next
