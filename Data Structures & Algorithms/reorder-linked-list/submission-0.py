# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # slow = middle of list
        # reverse linked list after slow

        curr = slow.next
        slow.next = None

        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        while prev and head:
            hnext = head.next
            pnext = prev.next
            head.next = prev
            prev.next = hnext
            prev = pnext
            head = hnext


            

            
            



