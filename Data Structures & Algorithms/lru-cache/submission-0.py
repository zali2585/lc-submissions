class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):

        # creates dictionary to store key/values
        self.capacity = capacity
        self.cache = {}

        # dummy nodes to mark least recently used(left) and most used(right)
        self.left = Node()
        self.right = Node()

        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        prevNode = self.right.prev
        nextNode = self.right

        # linking outer nodes to new 
        prevNode.next = node
        nextNode.prev = node

        # linking new to outer
        node.next = nextNode
        node.prev = prevNode

    # HELPER FUNCTIONS
    def remove(self,node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)

        return node.val
        

    def put(self, key: int, value: int) -> None:
        # if key is already in dict, removes it from current spot in queue
        # ...to update to most recently used
        if key in self.cache:
            self.remove(self.cache[key])
        # creates new node of key, value
        node = Node(key, value)
        # adds new node to dict.values
        self.cache[key] = node
        # attaches node to linked list of values
        self.insert(node)
        
        # if new node > capacity, removes lru
        if len(self.cache) > self.capacity:
            # left most node = lru
            lru = self.left.next
            # removes from linked list
            self.remove(lru)
            # deletes entry from dict
            del self.cache[lru.key]

