class Solution:
    def swapPairs(self, head):
        temp = head
        if not head or not head.next:
            return head
        temp2 = head.next
        prev = None
        while temp and temp.next:
            dum = temp.next.next
            temp.next.next = temp
            if prev:
                prev.next = temp.next
            temp.next = dum
            prev = temp
            temp = dum
        return temp2