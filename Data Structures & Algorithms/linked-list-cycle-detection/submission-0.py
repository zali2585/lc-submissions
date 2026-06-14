# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            # must iterate slow and fast first bc will always
            # return true at first node
            # there can be no cycle at first node already so ok to do
            slow = slow.next
            fast = fast.next.next 
            if slow == fast:
                return True
        return False
        