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

        # curr = beg of second list 
        # slow.next = None makes first list end
        curr = slow.next
        slow.next = None

        # prev = end of second list (after reversal)
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # for readability not necessary (now represents beg of second list)
        second = prev

        while second and head:
            # store next of first and second list to access later
            fnext = head.next
            snext = second.next
            # make 1st elem of first list point to 1st elem of second list
            # make 1st elem of second point to second of 1st list
            head.next = second
            second.next = fnext

            # move forward in both lists
            second = snext
            head = fnext


            

            
            



