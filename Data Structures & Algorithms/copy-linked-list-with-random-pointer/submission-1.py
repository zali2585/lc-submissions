"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
"""
LOGIC:
first pass: create copies (interlinked right after original)
    EX: a -> a' -> b -> b'
second pass: connect random connections
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        # creating copies (not connecting random)
        curr = head
        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next   
        
        # connecting random connections
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        # seperate lists
        # two ways to go about this, either traverse list and visit both og and copies, or only visit ogs and fix copies in that same pass
        # this solution is the first way, less recommended by chat
        """
        curr = head
        copyHead = curr.next
        while curr.next:
            nextNode = curr.next
            curr.next = curr.next.next
            curr = nextNode
        return copyHead 
        """
        curr = head
        copyHead = head.next

        while curr:
            copy = curr.next
            curr.next = copy.next

            if copy.next:
                copy.next = copy.next.next
            curr = curr.next
        return copyHead




        