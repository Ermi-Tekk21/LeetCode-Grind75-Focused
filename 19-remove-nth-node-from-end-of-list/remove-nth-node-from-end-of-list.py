

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)  # Dummy node to simplify edge cases
        dummy.next = head
        
        first = dummy
        second = dummy
        
        # Move `first` n+1 steps ahead to create the necessary gap
        for _ in range(n + 1):
            first = first.next
        
        # Move both `first` and `second` until `first` reaches the end
        while first:
            first = first.next
            second = second.next
        
        # Remove the nth node from the end
        second.next = second.next.next
        
        return dummy.next  # Return the head of the modified list