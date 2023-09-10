class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        smaller = ListNode(-1)
        greater = ListNode(-1)
        curr1 = smaller
        curr2 = greater
        temp = head
        
        while temp:
            if temp.val < x:
                curr1.next = temp
                curr1 = curr1.next
                
            else:
                curr2.next = temp
                curr2 = curr2.next
            temp = temp.next
        
        curr2.next = None
        curr1.next = greater.next
        return smaller.next
