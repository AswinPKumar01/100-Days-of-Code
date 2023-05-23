class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        pal_check = []

        while head:
            pal_check.append(head.val)
            head = head.next
        
        if pal_check == pal_check[::-1]:

            return True
        else:
            return False
