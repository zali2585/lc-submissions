# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        carry = 0
        while l1 or l2 or carry:
            # getting val of current place, if not possible, 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # since theres a carry once, it carries over to all future values
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            tail.next = ListNode(digit)
            tail = tail.next

            # can assign l1 to null, just cant access it 
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next






        
        