  class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:        

        curr = head
        for _ in range(k):
            if not curr: return head
            curr = curr.next
		        
        prev = None
        curr = head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        head.next = self.reverseKGroup(curr, k)
        return prev
