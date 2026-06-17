# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head

        slow = dummy
        fast = dummy

        # put fast pointer at element after nth from end
        # so that when u move slow, it stops element before nth
        for i in range(n + 1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        # removing next node
        slow.next = slow.next.next

        return dummy.next
        
        

        
